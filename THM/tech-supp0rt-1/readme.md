# boot:
1. scan -> 22 80 samba kebuka 
2. fuzz ada phpinfo wp indexhtml dll -> next coba samba creds nya anonymous dulu coba biar mirip2 kek ftp
3. smbclient -L //10.10.131.24/ -> ada sharename yg kebuka tuh websvr
4. sharename yg kebuka tuh websvr  -> smbclient //10.10.131.24/websvr -> get file disitu coba -> get namafile
5. cat isinya katanya ada path /subrion -> ama panel gitu
6. ada creds nya juga tapi pass nya di encrypt jadi magic -> ke cyberchef search aja magic decode aja
7. login aja kalau bisa cari exploit nya -> searchsploit subrion -> cari yg ada .py nya
8. cp aja terus pake -> dah dapet shell gabisa kemana mana jir -> coba revshell lagi pake nc -> gabisa juga ternyata
9. dah ls ls dir lain aja /wordpress nanti config php juga di cat
10. ada itu pw nya di config tapi ssh pake db uname gabisa -> ls /home aja -> pw nya dipake ke user itu


# PE: 
1. ls -la cat aja bash_history nya -> ls /tmp /opt dulu -> sudo  -l
2. ada iconv cari aja di gtfobins -> lfile arahin ke /root/root.txt tinggal run aja sesuai gtfo bin -> klaim flag
