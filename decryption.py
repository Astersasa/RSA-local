import math
import numpy as np
import random
import os
import re

def decrypt(l,d,n):
    s=''
    for i in l:
        s=s+(chr((i**d)%n))
    return(s)
def change(l):
    p = []
    for i in l:
        m=re.compile('\S*')
        h=m.search(i)
        p.append(int(h.group()))
    return p
te=open('ciper_list.txt','r')
l=te.readlines()
te.close()
p=change(l)
te=open('keys.txt','r')
l=te.readlines()
# h=change(l)
te.close()
h=change(l)
clear=decrypt(p,h[1],h[2])
os.remove("ciper_list.txt")
os.remove("ciper_word.txt")
os.remove("keys.txt")
te=open('password.txt','w')
te.write(clear)
te.close()