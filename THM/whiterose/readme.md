# boot:
1. ip sama web nya kudu di catet /etc/hosts dulu jir -> nmap scan aja 
2. fuzz dir ama subdomainnya -> nemu admin.domain -> masuk aja
3. pake credential di deskripsi -> explore web masuk message -> bisa idor ganti2 param id ?c=5 -> ganti ampe 7 8 dapet passwd
4. logout login ulang pake cred baru -> cari no hp tyler -> ke setting
5. coba ubah username passwd terus intercept burpsuite -> ganti password jadi typo misal passwrd -> buat trigger error ejs
6. https://eslam.io/posts/ejs-server-side-template-injection-rce/ -> buat exploit nya
7. ke revshells.com -> ke busybox nc -> pake ip port vpn  -> nanti di paste command nya ke exploit cve tadi 
8. jan lupa nyalain nc -> dan send payload tadi dari burp -> jan lupa pty disitu -> klaim user flag -> ini bukan www-data


# pe:
1. sudo -l -> disitu ada sudoedit sudoedit -> coba ini
2. https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudoedit-privilege-escalation/
3. export EDITOR="vim -- /etc/sudoers" -> jalanin sudoedit nya yang di sudo -l -> hapus nopasswd samain kayak root -> klaim root
4. ternyata export TERM=xterm tuh ada fungsinya -> biar vim nya ga error error
5. ctrl + z -> stty raw -echo; fg
6. di config sudoers tambahin aja -> user ALL=(ALL:ALL) NOPASSWD: ALL -> sudo su dah jadi
