1. versi :
- cek ke settings -> system -> about -> windows server 2016 -> version nya ambigu jir di soal

2. check the last user logon :
- event viewer -> windows logs -> security -> ke filter current log : 4624 event id nya
- nyari pakai event last hour gabisa jir filternya malah beda detailnya

3. check last john logon :
- ke cmd -> net user "John" | findstr "Last" -> dari wu ini

4. what ip system connect at first :
- antara cek di pas mulai start windows

- atau cek di folder Windows/system32/drivers/etc/host -> kek /etc/hosts lah ya
- banyak ip didalam apa dns poisoning y kata wu -> cek ke regedit -> key local -> software -> ms -> windows -> curr ver -> run
- itu kek buat ngecek gitu app apa yg jalan pas run -> keknya gitu

5. 2 acc had admin privilege :
- dari baca wu -> Get-LocalGroupMember -group "Administrators" 


6. schedule task that is malicious :
- Get-ScheduledTask | where{$_.TaskPath} -eq "\"} -> cari schedule task yang path nya ada di root \

7. file apa yg run daily dari schedul tadi :
- $tosk = Get-ScheduledTask | where Taskname - eq "Clean file system"
- $tosk.Actions -> nanti tau

8. what port this file did locally for :
- di Actions tertera sih itu nc -l nya di argument

9. when did jenny login last for :
- net user Jenny | findstr "Last"

10. what date did compromise take place :
- cek aja di folder c -> date ada di inetpub, tmp , users, windows

11. during compromise what time did windows special priv to a new logon :
- ke event viewer -> create event -> custom time range
- time range 4:00 pm 03/02/2019 -> sama aja sampai 4:30 pm
- next ceklist event logs -> ke windows security
- next cari aja yang sec group management -> nah di general ada logged nya edit aja date nya 2 jadi 02

12. tool was used to get windows passwd :
- mim.exe biasanya muncul -> dia di tmp -> cari aja di tmp
- cek mim out nya 
- itu nama tool nya

13. what was the attacker command control external ip :
- ke etc host -> disitu ada google.com -> coba ping google.com di windows sama mesin linux mu
- nah itu dia

14. what was the extension file of shell uploaded via web server :
- cek di inetpub -> wwwroot -> ada gif yg udah executable harusnya -> ada jsp yang masih source code2 an mungkin
- jsp java 

15. last port attacker opened :
- ke windows firewall -> inbound rules -> filter by group: run without a group 
- cek allow outside -> port and protocol

16. check dns poisoningm what site was targeted : 
- ke windows -> system32 -> drivers -> etc -> hosts -> nah yang ip nya beda itu google.com
- jawab aja itu   

