"""
cryptography.py
Author: Andreas Moberg
Credit: Payton (for mad math skillz), Ashwini Chauswerry

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

keystroke=input("Enter e to encrypt, d to decrypt, or q to quit:")

cryptm=[]


if keystroke=="e":
    mess=input("Message:")
    key=input("Key:")
    k=len(key)
    m=len(mess)
    cryptm=[]
    cryptk=[]
    encrypt=[]
    
    if m>k:
        count=key*int((m-(m%k))/k)
        trun=key[0:(m%k)]
        newkey=count+trun
    elif k>m:
        newkey=key[0:m] 
        print(newkey, message)
   
    for x in mess:
        cryptm.append(association.find(x))
    for x in newkey:
        cryptk.append(association.find(x))
    
    
    encrypt.append([sum(x) for x in zip(cryptm, cryptk)]
    
    
    
if keystroke=="d":
    mess=input("Message:")
    key=input("Key:")
    k=len(key)
    m=len(mess)
    cryptm=[]
    
    if m>k:
        count=key*int((m-(m%k))/k)
        trun=key[0:(m%k)]
        newkey=count+trun
    elif k>m:
        newkey=key[0:m] 
        print(newkey, message)
   
    for x in mess:
        for y in key:
            cryptm.append(associations.find(x)-associations.find(y))
    for x in cryptm:
        print(associations[x], end="")
    
elif keystroke=="q":
    ...
    print("Goodbye!")
    
else:
    print("Did not understand command, try again.")




