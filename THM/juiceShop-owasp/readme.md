1. Lets go on adventure :
-> cek review di jus apel ada email admin 
-> ke search button -> cari nanti ada query parameter search?q=output
-> cek review green smothie -> nanti dia mention replicator -> search gugel -> nanti star trek

2. Inject the juice :
-> ke login page admin -> inject sqli -> 'admin or 1=1-- -> di kolom email y, bisa juga lewat intercept burpsuite
-> salah deng -> langsung ' or 1=1-- aja ke kolom email / intercept burpsuite -> gausa pake admin
-> loggout login ulang pake akun gmail bender -> bender@juice-sh.op'-- -> gausah or soalnya akunnya dah ada -> comment aja passwd nya bisa lolos

3. Who brock my lock :
-> ke login -> download dulu seclists apt-get install seclists buat ngebrute force -> nanti jadiin payload intruder burpsuite -> pake best1050.txt
-> sizenya gede gajadi dah -> download payload nya di raw github aja -> kalau udah brute nya di email admin y
-> cari email jim -> forgot password pake email jim -> cari di google nama tengah kakak tertua di jim star trek

4. Ah dont look :
-> ke about me -> cek term condition yang ngarah ke /ftp -> download in beberapa yang .md -> nanti flag muncul di page juiceshop mu
-> flag 2 dah ada stepnya -> cuman ganti vowel  aiueo ke 0 -> login pake email mcafee
-> ke ftp tadi -> ke file json -> nanti url ganti ke .bak%2500.md -> nanti copy flag di halaman juice shop nya

5. Who s flying this think :
-> inspect element -> terus ke debugger , nah cek file main js -> klik {} nya biar rapi -> ctrl + f -> cari admin -> copy path -> login admin -> paste
-> buka burp -> intercept masuk ke keranjang -> forward sampai api nya /rest/basket -> send repeater -> ubah param /1 ke /2
-> masuk ke administration lagi -> pencet logo sampah ke yang ngasih rating bintang 5

6. Where did that come from :
-> masuk ke search bar -> inject xss -> <iframe src="javascript:alert(`xss`)"> -> pakai ` jangan ' soalnya gadapet flag tadi
-> masuk ke akun admin -> privacy -> last login ip -> intercept burp -> logout -> buat header True-Client-IP: payload xss nya -> headernya manual
-> login admin -> ke order history -> track order -> id= ganti ke payload xss -> refresh page

