# boot:
1. scan nmap banyak port
2. fuzz gada apa apa soalnya katanya aneh -> tambahin island -> ini dari baca wu soalnya males lama
3. gada apa apa di dalam ada text putih cek source aja 
4. fuzz lagi aneh lagi juga 2100 -> disitu gada apa apa suruh nyari .ticket
5. pake aja gobuster -x .ticket biar extension nya itu -> ini aneh lagi soalnya green_arrow jadi lama
6. dapet tuh file nya di base berapa gitu kata hint ke cyberchef aja
7. coba login ftp terus get file aja
8. get other user ama aa jpg noh yg sus -> coba steghide --info  gada apa apa di fotonya 
9. steghide extract -sf tanpa pass gada juga
10. pake stegseek namafile.jpg wordlist/rockyou ada -> coba steghide extract -sf pake password yg ketemu itu
11. ada file zip cek 1 1 ada catatan ama password buat si user yang di other tadi
12. login ssh aja coba -> klaim user flag


# PE :
1. sudo -l -> ada pkexec pkexec aja di gtfobins
2. klaim root


bonus:
1. sebenenrya yang stegseek tadi bisa di ganti hex edit di file foto yg rusak png leav me alon
2. hexeditor namafile.png -> nah ubah sesuai signatures nya portable network graphic
3. di fotonya ada password passphrase
