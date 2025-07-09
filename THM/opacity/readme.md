# boot:
1. scan port -> ada http dll 
2. fuzz pake yg small jngn common -> dapet /cloud
3. masuk ada file upload -> gabisa mentah -> sanitasi revshell gini -> sidi.php#.png 
4. python server ip:port/nama.php#.png -> ke upload -> open link in new tab aja
5. sambil nyalain nc dapet shell -> biasanya cek2 dulu di /opt /tmp coba2 aja di /home juga
6. ada di /opt coba nyalain python server di target -> wget ke dir mu
7. keepass2john nama >> output.hash -> john output.hash -> nemu cred nya -> keepassxc namafile
8. masukin passwd tadi -> pass manager ternyata -> aku pake keepassxc portable di github release nya 

# pe:
1. coba cat script.php disitu di folder dua butuh backupinc -> masuk lib dah -> cp backupinc php ke home/user
2. edit backupinc biar ada revshell yg di home -> rm yg di lib -> cp ke lib nyalain nc
3. pake revshell php shell exec -> taruh di paling atas aja -> dah rm yg di lib ->  cp yg home ke lib 
4. nyalain nc
5. klaim root

