# 1. web analysis

## What port is for the web server? :

- nmap aja pake -Pn soalnya mesinnya windows

## What port is for remote desktop service? :

- cek aja hasil nmap

## What is a possible password in one of the pages web crawlers check for?

- ternyata di paling atas robots.txt

## What CMS is the website using?

- cek fuzz dir umbraco

## What is the domain of the website?

- cek email beberapa, namaemail@namadomain.com, pake namadomain.com nya

## What's the name of the Administrator

- cek puisi nya di article, nanti copas aja yang monday monday

## Can we find find the email address of the administrator? :

- nama author puisi itu disingkat aja kayak john doe jadi jd@anthem.com

# 2. initial access

## Let's figure out the username and password to log in to the box.(The box is not on a domain)

- tanpa anthem.com, xfreerdp /u:username /p passwd /v ip
- pake sg:passwdnya

## Gain initial access to the machine, what is the contents of user.txt?

- THM{N00T_NO0T}, di desktop ada

## Can we spot the admin password?

- ChangeMeBaby1MoreTime, ada di C:\, nah dia hidden files, ke view di bar, nyalain hidden files
- nanti access denied juga, ke properties -> security -> edit -> nah add, pake users add nya -> add in si sg
- buka file nya

## Escalate your privileges to root, what is the contents of root.txt?

- THM{Y0U_4R3_1337}, ke administrator/desktop

