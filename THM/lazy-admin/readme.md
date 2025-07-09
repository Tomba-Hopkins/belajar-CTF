# boot:
1. scan nmap -> 22 80 -> fuzz /content -> cari exploit sweet rice
2. searchsploit sweetrice -> lagi -x pathnya -> yang backup tuh coba 
3. donglot aja -> cek isinya ada creds, coba pake exploit yang php itu code exec itu
4. bikin html lah pokoknya di isi revshell
5. firefox namafile.html -> nyalain nc -> login manager:Password123 -> cek cek terus di ads ada ga
6. ulang2 sampe ada -> kalau ada input gitu ke -> /inc/ads atau apa ya cek aja di docs nya
7. dapet revshell cek cek mysql gada apa apa ada creds rice:randompass aja tapi gada apa apa
8. ke /home klaim user.txt

# PE :
1. sudo -l bisa jir www-data dahal -> next cek file .pl nya dia jalanin /etc/copy.sh -> coba echo "test" ke copy.sh bisa
2. echo "revshell" > copy.sh -> jalanin yang di sudo -l -> tapi pake sudo biar bisa root -> klaim root
