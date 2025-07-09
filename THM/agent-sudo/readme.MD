1. scanning nmap -> buka http 80 di web -> ganti user agent ke C -> terus refresh
2. scanning ftp -> hydra -l chris -P /usr/share/wordlists/rockyou.txt ftp://10.10.74.215 -f -vV -o brute.txt -> terus login
3. get semua file nya -> get namafile, nanti kesimpen di dir -> cek file2 foto pake steghide --info 
4. satunya coba di ekstrak pakai binwalk yang cutie -> binwalk -e cutie -> zip2john 80.zip > hash.txt -> john hash.txt
5. yang cute pakai steghide --info -> stegcracker wordlist[Area51] cute -> login ssh pakai itu
6. download foto -> scp username@ip/letakfile /kirim/ke
7. reverse image -> cari aja foxnews alien autopsy nanti ada jawabannya
8. pas dah login ssh -> ke home soalnya itu previlege si james -> sudo -l
9. cari di ini : User james may run the following commands on agent-sudo:
    (ALL, !root) /bin/bash -> terus cari cve nya
10. ikutin instruksinya di exploit db

