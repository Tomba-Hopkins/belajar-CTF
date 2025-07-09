1. scan 80 22 lain lain kebuka sih -> fuzz bisa sebenenrnya explore sendiri juga bisa
2. ubah endpoint dari /gallery/gallery.html jadi /gallery aja -> nanti ada dir list
3. cuman ada catatan -> coba cek gallery explore photo -> endpoint /static coba di fuzz
4. dapet tuh catatan di fuzz /00 -> ada endpoint lago yg dihapus katanya apa gmn -> buka aja ada login page disitu 
5. view source code -> buka file js file js disitu coba login pake cred itu  -> ada catatan ftp gitu gitu
6. coba cari port yg kemungkinan ftp -> ftp ip port -> pake cred tadi -> ls -> get namafile -> cek satu satu
7. http.request.method==POST -> di wireshark file pcap nya -> cek yang http -> disitu ada cred catet aja
8. ssh kesitu -> klaim user flag -> sudo -l gabisa -> ke /home -> coba python3 http.server -> wget ke authenticator
9. dekompres pake upx -> upx -d ke authenticator nya -> strings authenticator nya -> nanti ada tuh di atas yang welcome
10. hash analyzer cred nya -> decode aja coba -> dapet cred su aja -> masuk foldernya valley
11. download pspy dari wget machine kita aja -> https://github.com/DominicBreuker/pspy -> kirim ke target
12. pspy buat lacak python mana aja yg gerak ps monitoring -> cat aja sumbernya
13. find aja file yang dimaksut -> find / -name 'base64*' 2>/dev/null
14. samperin file nya ubah isinya jadi reverse shell python -> arahin ke ip port vpn mu 
15. nyalain nc -> klaim root
