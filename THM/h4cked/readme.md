# 1. 
- analyze aja pake wireshark
- nanti usut aja dari atas -> ada brute ftp pokoknya 
- jenny:password123 -> login ftp dia ada di dir /var/www/html
- upload backdoor -> STOR shell.php
- shell bisa di download di -> ftp-data -> isi shell pentestmonkey -> ternyata itu jawabannya link shell pentest monkey
- check di psh ack -> disitu ada command yg dilakuin pas udah revshell
- hostname itu di belakangnya tomba@sebus -> hostname nya sebus
- backdoor yg stealthy adalah rootkit

# 2. 
- nmap aja ada ftp kan
- next brute ftp jenny nya gausah capslock 
- wordlist rockyou aja
- dah login ftp get shell nya -> nanti put shell nya ubah aja ip sesuain
- nc revshell aja -> ke web ip/shell.php aja
- dapet shell gada apa apa ini baca wu ternyata langsung su jenny passwd nya sama kayak ftp
- next sudo -l aja bisa root langsung sudo su
- klaim di /root/reptile 
