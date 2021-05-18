import numpy as np
import string
from creatorRSA import *



num_alfa = {i: chr(i) for i in range(128)}


alfa_num = {value : key for (key, value) in num_alfa.items()}


#print(alfa_num[" "])

def mapear(l,n,e):
    val=alfa_num[l];
    return (val**e)%n
    
    
def encriptar(mensaje,sec):
    
    n,e=getPUBLIC(sec)
    letras=list(mensaje.lower())
    numeros=[mapear(l,n,e) for l in letras]
    return numeros 
    
