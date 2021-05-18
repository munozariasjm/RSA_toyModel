import numpy as np
import math
def isPrime(k):
        ban=True
        for z in range(2,k): 
            if k%z==0: ban=False
        return ban

sec=100
def setSec(secs): sec=secs
def generarVals(numerito):
    
    
    e=65537
    p=11;q=17
    
   #primesP = [i for i in range(13,numerito) if isPrime(i) and i%e!=1]
    
    #p = np.random.choice(primesP)
   
    #primesQ = [i for i in range(17,numerito) if isPrime(i) and i%e!=1]
    #q = np.random.choice(primesQ)
    phi=(p-1)*(q-1)
    n=p*q
   
    
    while True:
        e=np.random.randint(2,phi/2)
        if p%e!=1 and q%e!=1: break
    e=3
    

    return n,e,phi






#print("public Key es: {}{}".format(n,e))
def getPUBLIC(sec=100): 
    n,e,f=generarVals(sec)
    return int(n),int(e)

i=np.random.randint(1,4)

#print("private Key es: {} ".format(int(d)))
def getPRIVATE(sec=100): 
    n,e,phi=generarVals(sec)
    
    d=((2*phi)+1)/e
    return int(d)
