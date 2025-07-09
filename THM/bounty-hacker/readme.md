# boot :
1. scan nmap 21 22 80 kebuka -> fuzz gada apa apa -> ftp login anonymous bisa tapi keknya cuman bisa jalanin 1 command dah
2. abis itu lag soalnya  -> next dapet wordlist gatau buat apa
3. ternyata buat bruteforce ssh -> di ftp ada catatan tadi get aja sih ada nama penulisnya
4. ama ada wordlist juga -> ssh in aja itu penulisnya pake password wordlist yang dikasih 
5. hydra -l lin -P locks.txt  ip ssh -t 4 -f -v 
6. klaim user flag

# PE :
1. sudo -l -> ada tuh tar cari aja di gtfobins tau passwdnya juga buat sudo kok
2. pake ini: sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
3. klaim root flag
