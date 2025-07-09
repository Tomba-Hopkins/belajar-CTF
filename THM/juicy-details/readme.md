# reconnaissance :
> tools: cek di access.log, tools ada header label nya misal (nmap) (sqlmap) (feroxbuster) (curl) (hydra) cek aja
> endpoint bruteforce: cek aja endpoint di acess log pas hydra, itu yg vuln brute
> endpoint sqli: cek aja di access log endpoint sqlmap
> param sqli: cek ? nya apa ?query= paramnya query, atau ?name paramnya name
> endpoint retrieve files: cek access log paling bawah dia mau cek /ftp ambil kupon gitu


# stolen data :
> section web to scrape user email: cek awal2 di access log dia scrape email di /products/id/reviews
> timestamp login success with bruteforce: cat aja access log nya | grep Hydra | grep 200, nah copas aja timestampnya
> victim retrieve from sqli: email password, cek aja di endpoint dia lakuin dios
> files try to download: cek di ftp, dia mau ambil .bak itu
> nama service dan uname for retrieve file : service ftp, cek log vsftpd di akhir dia user anon, jadi bug Anonymous username for ftp  
> nama service dan uname for gain shell : cek di auth log, dia ssh ke www-data
