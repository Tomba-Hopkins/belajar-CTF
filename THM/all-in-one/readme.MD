1. scan nmap 21 22 80 kebuka
2. dir fuzz -> ada wp lah pokoknya
3. baca W U ternyata vuln nya disini -> https://www.exploit-db.com/exploits/40290
4. lfi kesini 
5. ?pl=php://filter/convert.base64-encode/resource=/var/www/html/wordpress/wp-config.php 
6. upload shell abis itu di plugins editor -> terus ini /wp-content/plugins/akismet/akismet.php
7. dah dapet shell -> sebenernya cari di /etc/mysql/conf.d/ disitu ada private text isinya cred
8. tapi karna aku gatau langsung linpeas aja

PE:
1. linpeas ada bash suid tinggal bash -p jadi root
2. tapi manualnya sudo -l dulu -> ada socat tuh -> cari di gtfo yg socat -> sudo
3. dah run terus whoami aja -> klaim root
