import numpy as np
import string
from creatorRSA import *
from encrypting import *
from decrypting import *
import getpass


class BTC:
    mensaje="None"
    password=""
    
    def __init__(self,sec=100,n=0,e=0,password=""):        
        self.sec=sec
        self.n=n
        self.e=e
        
        print("*********************************************")
        print("*      Wellcome to RSA_Encryption BTC       *")
        print("*********************************************")
        print("*          by: Jose Miguel Muñoz            *")
        print("*********************************************")
        self.password=getpass.getpass("Insert your new password")
    def encrypt(self,mensaje):
        """
        Encrypts the message
        Input:
        'sec': Maximum security Measure
        
        Output: Encripted Message
       
         """
        print("*********************************************")
        print("Your Message is being encrypted")
        
        
        se=encriptar(mensaje,self.sec)
        print("Message succesfully encrypted!")
        return se
         
     
    def pEncrypted(self,mensaje):
        """
        Prints the encrypted message
        input: message to print
        output: None
        """
        print("*********************************************")
        print("Displaying encrypted message: ")
        print(encriptar(mensaje,self.sec))
        
        
    def decrypt(self,mensaje):

        print("*********************************************")
        print("Your Message is being decrypted")
        
        return desencriptar(mensaje,self.sec)
        
        print("Message succesfully decrypted!")
        
    def getPublicKey(self):
        print("This can be seen by anyone:")
        return getPUBLIC(sec)

    def setPassword(self):
        
        password=getpass.getpass("Insert the new password")
        
    def getPrivateKey(self):
        
        user = getpass.getuser()
  
        while True:
            pwd = getpass.getpass("User Name : %s" % user)
  
            if pwd == self.password:
                print("Welcome!!!")
                print("The private Key is ")
                print(getPRIVATE())
                break
            else:
                print("The password you entered is incorrect.")
                      
    
    
        