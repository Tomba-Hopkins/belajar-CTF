# boot:
1. scan nmap cek 80 sama 8080 -> fuzz aja gada apa apa -> next cek2 foto intinya kudu jpg jpeg -> strings nama | grep THM
2. pake https://github.com/joaomatosf/jexboss.git -> nanti tinggal run run aja
3. pake ampe yang jmxinvoker -> no no in aja -> lhost lport noh   
4. disini lah pokoknya : CVE-2015-7501  -> cari aja exploit github
5. ke user jboss -> ls -la ada bin run aja coba -> gada apa apa coba cat aja -> ada .file.txt cek aja
6. di note juga ada password -> su aja -> klaim user flag


# PE :
1. sudo -l -> cari sudo find di gtfo -> di hash base64 decode aja 
2. masih ga plain -> hasil decode cek di crackstation
3. klaim root
