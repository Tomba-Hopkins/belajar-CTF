# boot:
1. scan nmap 22 80 -> ke http cek source code -> ada jpg wget aja
2. jpg tapi di file png -> ubah hexeditor ganti jadi jpg signature
3. ke dir secret nya noh cepet
4. ?secret= 0-99 burp aja di intruder -> tau lah ini baca wu mumet bat
5. steghide extract sf aja jpg nya -> passphrase pake yangg di ?secret= tuh
6. foto yg di main quest thm badut itu trace aja -> ampe ke webnya jangan wget tapi download jadi jpg
7. dapet tuh steghide aja lagi tanpa passwd tapi dapet noh -> username nya ternyata rot13 coba aja
8. login ssh klaim root

# PE :
1. find / -perm -u=s 2>/dev/null -> dapet /bin/screen-4.5.0 -> cari aja exploitnya
2. tuh ada exploitnya wget aja ke victim ama run kyk yg di github ->  klaim root
