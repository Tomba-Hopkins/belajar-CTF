# boot:
1. scan nmap 21 kebuka login aja Anonymous -> next cek 8081 webnya disitu
2. di 21 ada pesan gitu kaitannya ama cve -> coba aja dah cve nya 
3. INGET: ini berjam jam gabisa upload gegara salah namain domain di /etc/hosts -> harusnya magician aja gausa magician.thm
4. coba aja nanti bisa upload png lancar
5. next ubah aja source code nya -> dari https://imagetragick.com/ yang no 5
6. dia kan etc/passwd -> ubah aja jadi '| revshell ' -> langsung aja sih vim revshell.png gitu gausa convert2
7. dapet shell dari revshell -> klaim user flag aja udah

# pe: 
1. coba linpeas soalnya nyari2 di /opt bash_history gada yg sus -> mungkin jar nya sus tar dicoba dulu
2. di linpeas ada ginian:
 will not be shown, you would have to be root to see it all.)
tcp        0      0 127.0.0.1:6666          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8081            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::8080                 :::*                    LISTEN      1292/java           
tcp6       0      0 :::21                   :::*                    LISTEN      -  
3. di the_magic_continues juga katanya gitu clue nya
4. ada service terrsembunyi -> kira2 ada backdoor 
5. di curl 127.0.0.1:6666 pas di mesin target ada tuh response nya
6. mkfifo /tmp/f; nc -lvp 7777 < /tmp/f | nc 127.0.0.1 6666 > /tmp/f  -> ini bakal nge forward local:6666 di target jadi       ke 7777 biar bisa di akses dari luar
7. ato ganti 6969 juga bisa -> nanti aksesnya http://magician:6969   
8. nyalain port forwarding kayak tadi itu di mesin target  -> dah akses /root flagnya di web -> klaim root
9. gagal jir tau lah -> download socat disini aja nanti wget dari python servermu: 
https://github.com/andrew-d/static-binaries/tree/master/binaries/linux/x86_64
10. jalanin gini di mesin targett: ./socat tcp-listen:6969,reuseaddr,fork tcp:localhost:6666
11. nanti akses magician:6969 bisa tuh -> klaim root dari backdoor
