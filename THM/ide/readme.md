# boot:
1. scan nmap -> 80 21 kebuka port tinggi web nya -> login users di fuzz aja semua 80 ama port tinggi
2. gada gada -> ftp ip port -> ls -la -> cd ... -> get tuh - nya -> get -
3. cat aja katanya default password -> john:password 
4. tau cred nya bisa cari cve nya -> download aja exploit nya -> kasih opsi  url ipmu portmu platformmu
5. nyalain 2 nc -> 1 seperti yg disuruh ada bash bash nya -> 1 lagi murni nc
6. ke /home/user -> cat .bash_history -> ada catatan cred tuh -> coba su kesitu pake passwd itu

# pe:
1. sudo -l -> vsftpd nyala -> ls -la /lib/systemd/system -> disitu ada .service -> ubah aja
2. ubah jadi reverse bash shell -> /bin/bash -c 'revshel'->  execstartnya -> nyalain nc dan restart yg di sudo -l nya 
3. ternyata suruh systemctl daemon-reload dulu lakuin aja -> restart yg di sudo -l nya -> klaim root

