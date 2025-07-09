# boot:
1. scan nmap 22 80 kebuka fuzz gada apa apa ada admin login page aja
2. bingung dan baca wu ternyata vuln ada di code login js nya
3. buat cookies baru SessionToken isinya bebas path nya / refresh -> dapet rsa key ssh aja
4. ssh buat james -> coba dulu aja -> gabisa ssh2john dulu aja kalau gitu -> dapet passphrase
5. klaim user flag

# PE :
1. linpeas writeable -> /etc/hosts cron job cek juga
2. ubah /etc/hosts yang hostnya di curl ama cron jadi ipmu
3. buat folder downloads/src/buildscript.sh yang isinya revshell di mesinmu bukan di target
4. python http server 80 di luar downloads + nc in port yg di revshell nanti gausah curl salahku curl tadi
5. connect2 sendiri -> klaim root
