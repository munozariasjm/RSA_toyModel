import numpy as np
import string
from creatorRSA import *
from encrypting import *

def setPUBLIC(a,b):
    n=a;e=b
def des_mapear(val,sec):
    d=getPRIVATE(sec)
    n,e=getPUBLIC(sec)
    
    return (val**d)%n

    

def desencriptar(mensaje,sec=100):
    d=getPRIVATE(sec)
    n,e=getPUBLIC(sec)
    
    listaM=[des_mapear(l,sec) for l in mensaje]
    
    lMen=[num_alfa[k] for k in listaM]
    
    
    return "".join(lMen)