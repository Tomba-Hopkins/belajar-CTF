# boot:
1. scan nmap 22 80 ada -> fuzz ada sitemap ama cek source code ada msg buat user
2. fuzz lagi di dalem sitemap ada .ssh -> wget rsa nya -> chmod 600 -> ssh -i ke user tadi
3. klaim flag

# PE :
1. sudo -l -> cari wget cobain 1 1 ada di fileupload ternyata 
2. set aja kayak nc ama lokasi file gitu gitu -> flag nya ga root.txt -> samai kek user txt coba pattern nya
3. klaim root
