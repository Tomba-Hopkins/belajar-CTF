1. scan nmap ada 80 22 sama pop3
2. cari2 aja fowsniff di gugel ada github isinya leak creds 
3. decrypt 1 1 aja kumpulin hash passwd nya atau jadiin username:passwd gitu gatau lah 1 1
4. di crackstation juga bisa atau cyberchef serah dah serah
5. dah dapet pisahin uname sama passwd -> ke msfconsole pop3 login search aja options ke uname_file ama passwd_file
6. set aja run dapetin creds -> dapet pop3 nanti ads LIST buat command pop3
7. dah dapet login dari nc ternyata -> nc ip port_pop3 -> User usernamenya -> Pass passwdnya
8. dapet tuh RETR1 -> ada apa gitu cek aja dah -> RETR 2 juga cek aja dah cek cek
9. dapet tuh creds login ssh -> cek2 gada apa2 cek /opt ada file sh rewriteable -> edit revshell aja python3 -c aja
10. itu di /etc/update-motd.d -> dah pasang shell ssh lagi aja sambil nyalain nc -> klaim root
