# boot:
1. scan nmap -> 21 22 80 kebuka -> 
2. fuzz -> ada /files ternyata ftp bisa di akses di http jadi bisa taruh shell
3. pake -> put namashell.php -> buka filenya
4. dah dapet shell cek / ada incident -> ambil pcap nya
5. cari di wireshark disini -> tcp.stream eq 7 dah ada creds disitu
6. ssh kesana dah dapet userflag -> kalau bumbu2 ada sih di linpeas cari aja


# pe:
1. ada scripts -> cat aja dia pake /etc/print.sh -> ubah print.sh jadi
2. echo "revshell" >> /etc/print.sh -> run yg di script nc -> klaim root
