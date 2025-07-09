1. file namafile -> ada yg salah
2. 0x41haz-1640335532346.0x41haz: ELF 64-bit MSB *unknown arch 0x3e00* (SYSV) -> gitu awalnya
3. ganti bit ke 5 dan 6 dari 02 jadi 01 01 -> nanti jadi gini
4. 0x41haz-1640335532346.0x41haz: ELF 32-bit LSB shared object, x86-64, version 1 (SYSV), no program header, no section header
5. ternyata bit ke 6 aja yg di ganti jadi 01, nanti jadi gini :
6. 0x41haz-1640335532346.0x41haz: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6c9f2e85b64d4f12b91136ffb8e4c038f1dc6dcd, for GNU/Linux 3.2.0, stripped
7. dah chmod +x app ELF nya -> r2 ./elfnya
8. aaa -> alf -> pdf @ main -> cari dah string nya


tambahan:
1. elf itu exe di linux
2. r2 dipake buat baca file exe atau elf -> nanti bisa liat fungsi2 file ini tapi dalam bahasa assembly

