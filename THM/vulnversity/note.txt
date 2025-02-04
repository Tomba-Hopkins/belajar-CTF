1. recon scanning : nmap -sV -p- ip --min-rate 1000 -vv -> jawab aja semuanya
2. fuzz: ffuf -w /dirbuster/dirlist-1.0.txt -u ip:port/FUZZ -fw 18
3. upload shell: upload reverseshell -> burpsuite intruder with wordlist -> uncentang encoding nya -> attack -> nc and gain shell
4. previlege escalation: find / -perm -u+s -type f -exec ls -l {} \; 2>/dev/null -> service issue di systemctl
-> tanya gpt, buat shell .service yang pake ip port attacker -> nyalain nc -> nyalain systemctl shell tadi -> klaim root
