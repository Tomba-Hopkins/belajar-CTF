# boot:
1. scan nmap: 21 22 80 100 106 109 110 111 113 (baca info disini) 119 125 
2. dapet path ke path -> wget aja -> dapet file binary -> strings namafile
3. ada key -> ke ftp ada file foto get aja login Anonymous aja ->  steghide extract -sf namafoto -> key nya tadi
4. ternyata key nya gabisa  gatau buat apa -> steghide --info namafoto -> nanti Y aja disitu ga perlu masukin passphrase
5. isinya b64 decode aja  -> cuman etc shadow ternyata -> fuzz dir lagi gobuster nya tambahin -x .php
6. nemu tuh bisa run command -> revshell aja
7. masuk di www-data -> cat aja semua file disitu kali aja ada creds 
8. dapet creds dan tau g -> ternyata itu creds buat login web
9. dan akses ke web ternyata ke php yg di fuzz itu -> gas ke home cat semua nya ada id rsa tuh
10. pake aja id rsa ke ssh charlie -> klaim user flag

# PE:
1. sudo -l -> ada vi -> cari aja di gtfobin yg vi yg sudo -> jadi sudo ke root
2. ternyata flag di .py -> run suruh masukin key -> pake key yang di file keyrev tadi -> 'keyrev'
