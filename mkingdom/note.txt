1. scan 85 buka -> masuk aja
2. fuzz dir nemu /app -> masuk aja -> ke castle explore ada log in di footer
3. cari default cred -> ada disini
4. https://archive.concretecms.org/community/forums/installation/admin-username-email-login-problem-solved./
5. kalau gabisa ya coba2 aja default2 admin password -> explore
6. ada fitur upload file -> cek allow di setting ubah biar ada php -> upload shell -> buka nc buka yg di upload 
7. nanti munucl sendiri link nya -> buka aja dah jadi www-data -> explore /var/www/html 
8. di project castle -> di config ada creds -> masuk /home/user -> coba ketik env -> ada jir creds disitu base64 decode aja
9. ke user 1 nya -> ada user flag gabisa di cat -> pindahin ke /tmp aja terus cat
10. di pspy ada yg jalan -> di linpeas /etc/hosts nya bisa digonta ganti -> bikin aja revshell bash
11. kan di pspy bilang dia bakal curl ke url:85/app/castle/application/counter.sh -> buat aja imitasinya
12. counter.sh ama folder semua itu di mesin mu -> isinya revshell tapi
13. di victim tinggal ganti /etc/hosts ganti nya di /etc jangan di home -> ipmu namadomainurl yg di curl tuh
14. nyalain python3 http.server di luar /app -> nyalain nc port di revshell bash nunggu dapet root -> klaim root
15. flag root di /tmp juga pindahin
