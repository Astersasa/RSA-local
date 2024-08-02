import math
import numpy as np
import random
import os

def is_prime(n):
    flag=1
    for i in range(2,int(round(math.sqrt(n),0)+1)):
        if (n%i)==0:
            flag=0
            break
    return (flag)

#generate the prime integer p and q
def pq_generate():
    p=random.randint(3,20)
    q=random.randint(3,101)
    while (not(is_prime(p))) or (not(is_prime(q))):
        p=random.randint(3,20)
        q=random.randint(3,101)
    return(p,q)

#calculate the value of totient function
def totient(p,q):
    return((p-1)*(q-1))

#check whether two numbers are coprime
def co_prime(a,b):
    if math.gcd(a,b)==1:
        return(1)
    else:
        return(0)

#generate e
def e_generate(n):
    e=random.randint(3,n)
    while not(co_prime(e,n)):
        e=random.randint(3,n)
    return(e)

def ext_gcd(a,b):   
    if b == 0:          
        return 1, 0, a     
    else:         
        x, y, gcd = ext_gcd(b, a % b)        
        x, y = y, (x - (a // b) * y)    
        return x, y, gcd    

def d_calculate(e,wn):
    #Extended Euclidean
    x,y,gcd=ext_gcd(e,wn)
    #make sure d is positive number
    if x<0:
        x=x%wn
    return(x)

#generate prameters for RSA algorithm
def parameters_generate():
    p,q=pq_generate()
    n=p*q
    wn=totient(p,q)
    e=e_generate(wn)
    d=d_calculate(e,wn)
    #make sure d and e are different
    while d==e:
        parameters_generate()
    return (e,d,n)

def intc(m):
    n=[]
    for i in m:
        n.append(ord(i))
    return(n)

def encrypt(list,e,n):
    l=[]
    s=''
    for i in list:
        l.append((i**e)%n)
    for i in l:
        s=s+str(i)
    return(s,l)

# def decrypt(l,d,n):
#     s=''
#     for i in l:
#         s=s+(chr((i**d)%n))
#     return(s)


# In[143]:


#the main code for encryption
e,d,n=parameters_generate()
te1=open('keys.txt','w')
te1.write(str(e))
te1.write("\n")
te1.write(str(d))
te1.write("\n")
te1.write(str(n))
te1.close()

# In[144]:


#input and send -----client
# clear_message=input("please input your message for encryption:")
te=open('password.txt','r')
clear_message=te.readline()
te.close()
#change the text to the intger based on ascii code
cm_list=intc(clear_message)
#encrypt the clear_message
ciper_message,l=encrypt(cm_list,e,n)
os.remove("password.txt")
te=open('ciper_word.txt','w')
te.write(ciper_message)
te.close()
te=open('ciper_list.txt','w')
for i in l:
    te.write(str(i))
    te.write("\n")
te.close()
# print(ciper_message)


# In[145]:


#decrypt--------serve
# te=open('ciper_list.txt','r')
# l=te.readline()
# te.close()
# clear=decrypt(l,d,n)
# print(clear)


# In[ ]:




