# boot:
1. scan nmap 22 80 kebuka -> tapi 22 malah http 80 malah ssh
2. buka aja di firefox -> about:config -> network.security.ports.banned.override
3. kalau gada plus aja ke string -> tambahin 22 kesitu -> buka aja http://ip:22 
4. ada password katanya -> ada /recovery.php juga
5. ada msg juga -> ke login page gabisa passwd nya -> coba steghide extract 
6. ke fotonya passphrasenya yang di password itu base64 pokoknya yang di source code
7. dah dapet creds buat login bisa revshell itu yang ?cmd=revshell_pake_urlencode
8. dah dapet revshell -> jadi www data -> ke /opt ke /var/www gada apa apa
9. ke /home ada tuh cat aja -> ada wordlist buat jack
10. brute aja ssh nya -> hydra -l jack -P wl.txt ssh://10.10.32.185:80
11. su -> gada flag.txt ada nya jpg
12. coba ambil aja dulu -> scp -P 80 jack@ip:/home/jack/user.jpg .
13. diliat fotonya jir -> kalau mau simple cari aja image to text converter
14. klaim user flag 


# PE :
1. sudo -l gabisa -> /opt gada -> find / -perm -u=s 2>/dev/null ada strings
2. cari di gtfo -> ada strings -> LFILE=/root/root.txt -> string "$LFILE"
3. klaim root
