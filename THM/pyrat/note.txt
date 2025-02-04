1. scanning port -> 80 gada coba ke 8000
2. kata dia gabisa koneksi biasa -> coba curl -v ip:8000 -> gabisa 
3. coba telnet ip 8000 -> bisa coba nc ip 8000
4. print(1) -> dia masuk -> dan di curl kan dia bilang dia python
5. cari rev shell python -> https://www.revshells.com/ -> masukon aja ip port disitu sambil nc nyala -> gapake python -c
6. cari di /opt/dev disitu ada .git ls -la aja -> config nya coba di cat -> disitu ada cred -> coba login ssh
7. cred think:_TH1NKINGPirate$_
8. klaim user flag -> ke /opt/dev -> git status -> git restore namafile -> cat 
9. logout -> baca wu aja di medium -> ada script bruteforce nya -> dah nemu passwdnya baru
10. nc ip 8000 -> admin -> suruh masukin passwd masukin passwd tadi -> klaim root
