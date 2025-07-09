1. download source code -> analyze dulu 
2. ada -> admin&password=sUp3rPaSs1
3. run lewat nc aja ke ip mereka biar ga error2 package gada
4. coba masukin creds disitu -> pasti not easy -> ganti digit 1 di  username nya bdmin:password_tadi 
5. nanti jadi tau hash aslinya gimana 
6. misal c779c58a9c4f7df2c691999cf26b8c3bfd7513152c5704f01279e1cc3269588bda9b2c6b5f48d62faa0b255703049fdd,
7. ambil 32 digit ke 1 + 32 digit ke 2
8. jadi: c779c58a9c4f7df2c691999cf26b8c3b + fd7513152c5704f01279e1cc3269588b
9. digit 1 -> c7 | digit 2 -> fd -> xor in -> a xor dec(b) -> c7 xor dec(fd)


-> DAH DAH BUBAR gini caranya
1. ambil 1 digit huruf awal misal : 22919bee9626c47540edb82aaae016f2d76e05726fbb38a48bd9eea7b30c1083a4f4a6431763f331721bde33b59bd33f
2. jadi ambil digit1: 22 -> 22 xor hex huruf b -> 22 xor 62 
3. hasil XOR hex huruf a -> hasil XOR 61 -> nah tinggal digit 1 edit aja
4. misal 22 91 9b -> jadi ->  24 91 9b ...danseterusnya
5. klaim dah flag nya 

