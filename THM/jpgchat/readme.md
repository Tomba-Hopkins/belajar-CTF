# boot:
1. scan nmap ada 22 ama ppp -> nc ke ppp atau web ke ppp -> terus [REPORT] atau atu
2. cari di google -> JPGChat site:github.com -> download source code 
3. nc ke ppp -> langsungg [REPORT] nanti dia ambil bash
4. revshell pakai yangg di encode https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/#bash-tcp
5. coba aja dulu -> udah ke upload revshell tapi whoami ama id gabisa gabisa command
6. revshell lagi sekarang yg biasa -> dah dapet shell noh -> o iya yg nc ke port ppp jan di close 
7. klaim user flag

# PE :
1. sudo -l ada ENV PYTHONPATH -> sama file sudo -l nya noh coba cat dulu isinya apa -> dia import compare
2. cd /tmp -> export PYTHONPATH=$PWD -> buat compare.py -> #env sama -> os.system('/bin/bash') import os
3. chmod +x compare nya ->  sudo [yg di sudo -l] -> klaim root
