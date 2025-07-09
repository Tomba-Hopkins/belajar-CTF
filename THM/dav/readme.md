# boot:
1. scan nmap cuman ada 80 -> next fuzz ada webdav -> ternyata di wu webdav ada default creds
2. http://xforeveryman.blogspot.com/2012/01/helper-webdav-xampp-173-default.html
3. cek aja defaultnya -> login
4. ternyata creds yg di dir list ga guna bjir wampp xampp itu 
5. cadaver [path_dirlistnya] -> put revshell nanti 
6. dah nanem -> buka aja sambil nc
7. langsung bisa ke /home user ls -la sudo -l juga 
8. klaim user flag

# PE :
1. sudo -l -> cari cat gtfo -> ada langsung cek root aja atau .bash_history disitu juga ada nama root.txt
2. klaim root
