#  user.txt :
> cek semua dulu fuzz nmap, cuman 80 ssh
> fuzz ada /r -> follow aja ampe /r/a/b/b/i/t
> dia kek nyuruh rabbit in, ato foto awal yang rabbit itu di steghide extract -sf aja, di hint.txt dia juga nyuruh gitu
> ampe ujung kosong cek source code, ada creds login ssh aja
> gada bjir

# user +  root.txt :
> sebenernya pake PwnKit bisa, tinggal run aja dah jadi root, tapi ada task2 lain yg butuh manual
> sudo -l -> ada ini (rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
> dia bukan alice tapi rabbit jadi run as rabbit
> ls baca code, dia import random, bikin revshell di file random, biar import ke yg di run itu
> dah revshell aja nanti as a rabbit ls ke dir home nya
> ada app tea, kalau di run dia ada date nya
> set lewat /tmp/date, bikin aja jadi /bin/bash aja,
> nah misal bikin di /tmp, export path dulu biar dia jadi bin yg run dimana mana
> sama chmod +x jangan lupa ke app date
> export PATH=/tmp:$PATH, nanti run aja app nya
> ke dir hatter, ada passwd, ls -la punya siapa itu, buat ssh ke hatter, ssh aja biar enakan
> pake linpeas lagi dah pake linpeas lagi, ada getcap tuh di linpeas
> getcap -r / 2>/dev/null, ada perl
> cek gtfobins yg perl, yg cap soalnya ada
> /usr/bin/perl  -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'
> klaim root, find find in aja flag nya
