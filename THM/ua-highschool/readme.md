1. scan port -> 22 80 kebuka -> buka web nya -> fuzz pake gobuster dir -> ada /assets fuzz lagi
2. dapet dah index.php di /assets -> fuzz parameter burp pake ffuf 
3. ffuf -u "web?FUZZ=id" -w wordlist/burpparam.txt -fs 0 | tee burpfuzz.txt
4. command injection bisa -> encode ke urlencode command nya -> command nc reverse shell yg mkfifo
5. encode ke url dan coba masukin sambil nyalain nc -> ambil ke /images yang oneforall -> wget aja ke url/assets/images/img
6. install xxd buat baca hex -> dari github vim aja /src/xxd/xxd.c -> compile -> gcc xxd.c -o xxd
7. ./xxd namafoto | head -> ubah hex baris 1 jadi jpeg signature file -> https://en.wikipedia.org/wiki/List_of_file_signatures
8. ubah dulu aja pakai hexeditor -> file namafile -> udah jadi jpeg jfif noh 
9. steghide extract -sf namafile -> butuh phrase ada di /var/www di file nya hidden content coba cat -> base64 decode aja
10. dapet creds -> ssh kesitu pake creds -> klaim user flag
11. sudo -l -> ada tuh yang di /opt -> jalanin pake sudo -> h >> test -> kesimpen -> coba bikin authorized keys di ssh root sshkeygen
12. yg id rsa pub gantiin auhtorized keys target ->  ssh ke root -> klaim root flag
