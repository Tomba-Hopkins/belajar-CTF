1. scan nmap banyak yg kebuka -> nc ip port nya yg 9009 tuh -> minta apa bilang certificate, minta apa bilang key
2. catet semua -> socat stdio ssl:10.10.53.65:54321,cert=certif.crt,key=prvkey,verify=0
3. masuk ketik passwd -> catet creds ssh kesitu
4. klaim flag -> sudo -l -> certutil ls -> sudo certutil -a fred noh -> catet ulang dari socat tadi -> passwd -> ssh lagi
5. sudo -l -> jalanin coba nanti dapet hash -> itu -> base64 base32 base64 md5 decrypt -> coba aja di cyberchef -> klaim root

