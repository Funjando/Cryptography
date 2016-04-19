"""
cryptography.py
Author: Andreas Moberg
Credit: Payton (for mad math skillz), Ashwini Chauswerry, UncleZiev

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

keystroke=input("Enter e to encrypt, d to decrypt, or q to quit:")




if keystroke=="e":
    mess=input("Message:")
    key=input("Key:")
    k=len(key)
    m=len(mess)
    cryptm=[]
    cryptk=[]
    encrypt=[]
    tencrypt=[]
    
    if m>k:
        count=key*int((m-(m%k))/k)
        trun=key[0:(m%k)]
        newkey=count+trun
    elif k>m:
        newkey=key[0:m] 
        print(newkey, message)
   
    for x in mess:
        cryptm.append(associations.find(x))
    for x in newkey:
        cryptk.append(associations.find(x))
    
    
    encrypt.append([sum(x) for x in zip(cryptm, cryptk)])
    
    for x in encrypt:
        tencrypt.append(associations[x])
    print(tencrypt)
    
    
if keystroke=="d":
    mess=input("Message:")
    key=input("Key:")
    k=len(key)
    m=len(mess)
    cryptm=[]
    cryptk=[]
    decrypt=[]
    
    if m>k:
        count=key*int((m-(m%k))/k)
        trun=key[0:(m%k)]
        newkey=count+trun
    elif k>m:
        newkey=key[0:m] 
        print(newkey, message)
   
    
    
    decrypt.append(x-y for x, y in zip(mess, newkey))
    
    #decrypt.append([sum(x) for x in zip(cryptm, cryptk)])
    
    print(decrypt)
    
elif keystroke=="q":
    ...
    print("Goodbye!")
    
else:
    print("Did not understand command, try again.")




