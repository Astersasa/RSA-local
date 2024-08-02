import math
import numpy as np
import random
import os
import re

def decrypt(l,d,n):
    s=''
    for i in l:
        s=s+(chr((int(i)**d)%n))
    return(s)
def change(l):
    m=re.split(' ',l)
    m=list(filter(None, m))
    return m

def keys(l):
    p = []
    for i in l:
        m = re.compile('\S*')
        h = m.search(i)
        p.append(int(h.group()))
    return p

#get keys
te=open('keys.txt','r')
l=te.readlines()
te.close()
h=keys(l)

te=open('ciper_list.txt','r')
l=te.read()
l=re.split('\n',l)
l=list(filter(None, l))
te.close()

if os.path.exists('decrypt text.txt'):
    os.remove("decrypt text.txt")
for i in l:
    p=change(i)
    clear=decrypt(p,h[1],h[2])
    te=open('decrypt text.txt','a')
    te.write(clear)
    te.write('\n')
te.close()