1. crackme1 :
- tinggal wget aja file nya -> dah chmod +x namafile -> ./namafile -> dapet flag

2. crackme2 :
- wget file nya -> cari passwd coba strings aja -> strings namafile -> ada tuh keknya  -> chmod +x namafile -> ./namafile passwdnya

3. crackme3 :
- wget -> strings aja file nya -> strings namafile -> ada base64 decode aja -> dah bisa usage juga sih -> ./file passwd

4. crackme4 :
- wget -> pakai ltrace ./namafile test -> nanti ada passwd nya
- strings itu buat cek permukaan
- ltrace buat cek program ngomong ke library -> buat cek runtime analyst lah

5. crackme5 :
- pakai r2 bisa -> r2 ./namafile -> aaa -> s sym.main -> pdf -> nanti ada char2 gitu urutin aja -> elf phdr itu @ disitu
- pakai ltrace bisa -> ltrace ./namafile -> enter aja -> test -> nanti ada jawabannya test aja


6. crackme6 :
- pakai r2 -> r2 ./namafile -> aaa dulu -> s sym.main -> pdf -> cek ada fungsi compare passwd
- s sym.compare_passwd -> pdf -> cek2 ada my_secure test noh fungsi baru 
- s sym.my_secure_test -> pdf -> nah disitu ada cmp al -> compare 8 bit kebawah apa gimana gatau ini baca wu
- nah nanti itu ada hex hex nya -> ke hex to ascii aja misal 0x33 nanti decode, semua cmp decode aja

7. crackme7 :
- pakai r2 -> r2 ./namafile -> aaa -> pdf -> ke main s sym.main -> ada func flag2 coba kesana
- s sym.namafunc -> pdf -> gada apa apa 
- baca wu ternyata di func main -> di atas ada kayak cmp ke hex 
- decode hex nya ke decimal -> masukin pas app nya run 
- disitu ada eax, var input -> nah dia compare input [var eax] sama salah satu hex, jadi kemungkinan hex itu passwd (dari gpt)
- ibarat -> i = input; if i == 0xflag; return flag

8. crackme8 :
- pakai r2 gabisa -> pakai ghidra -> masukin elf nya ke project ghidra
- analyze -> analyze all aja -> next cari func main -> cek decompiler -> nah nanti cek yg akses granted ada if ===
- next decode hex ke decimal -> nanti masukin -> -angkanya 

