# boot :
1. scan nmap ftp kebuka ssh http -> 21 22 80 kebuka next ke ftp login anonymous
2. fuzz gada apa apa -> get file ftp nya -> decode base4 -> masih ada cipher -> coba ke cipher identifier ada tuh
3. decode aja coba di vigenere solver -> ketemu dah itu passwd buat si pertanyaan
4. ssh aja kesana cek isi gada user flag
5. priv esc horizontal -> cek2 di /opt ls -la aja ada script cek isinya ngambil dari file lain
6. taruh revshell di file lain itu nanti otomatis script nya jalan kesitu
7. inget revshell nya sesuain ama shell situ -> which $SHELL -> kalau /bin/bash ya /bin/bash
8. gagal2 mulu dah keknya depannya kudu dikasih ; dulu atau hello && python -c "revshell" gitu 
9. intinya depan kudu triger dulu keknya dah 
10. setelah sekian lama ternyata benar -> kasih ; dulu di sebelum revshel -> echo "; revshell" > .quotes
11. klaim flag


# PE :
1. di linpeas ada vuln di users information
2. auk ah bingung baca wu aja -> di email3 ada tuh secret text ama yang di capslock key nya
3. decode aja vigenere
4. sudo su aja -> su root atau 
5. klaim root ada di email
