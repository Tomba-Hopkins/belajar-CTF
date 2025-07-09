# boot:
1. scan nmap 21 22 80 kebuka fuzz gada apa apa  source code di title ada ini: team.thm
2. masukin aja ke etc hosts dulu biar nanti bisa di subdom enum
3. dah subdo enum ada subdo dev masuk aja -> ada link juga -> di url ada param tuh kali aja bisa lfi
4. http://dev.team.thm/script.php?page=../../../../../etc/passwd -> bisa ternyata
5. ke /home/user/.ssh/ id rsa ama authorized keys gada di 2 2 usernya -> di bash history juga gada -> di access log juga gada
6. baca wu katanya /etc/ssh/sshd_config disitu letaknya 
7. cek aja dah -> ada tuh coba tapi edit dikit rsa nya soalnya ada # nya ssh kesitu 

# pe: 
1. linpeas aja -> dapet pkexec nya vuln
2. banyak sih yg vuln 
3. dah pake exploit pkexec punya orang -> klaim root
