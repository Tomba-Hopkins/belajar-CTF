1. scan nmap 80 ama berapa gitu kebuka -> next fuzz ada hidden ada nama nama user
2. next coba wpscan -> catet list user2 nya brute aja wp nya
3. wpscan --url http://10.10.179.7/ -U users.txt -P /usr/share/wordlists/rockyou.txt
4. masukin cold aja lah, ngapain buang2 waktu ngebf bjir
5. dapet usernya next login aja -> ke plugins editor -> ganti akimet misal dengan revshell pentestmonkey php
6. terus nc lalu ke ->  http://10.10.179.7/wp-content/plugins/akismet/akismet.php  
7. di linpeas ini oren -> /usr/bin/find -> mungkin cari di gtfo aja 
8. inget kalau gada file find gabisa ./ jadi find aja gitu -> binbash nya pake -p biar ga drop pangkat pas jalanin hak root
9. klaim all flag 
