"""
cryptography.py
Author: Andreas Moberg
Credit: Payton (for mad math skillz), Ashwini Chauswerry, UncleZiev, Alejandro

Assignment:

Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

#print(len(associations))
#85

keystroke=input("Enter e to encrypt, d to decrypt, or q to quit:")

quit=False

if keystroke not in ["e", "d", "q"]:
    print("Did not understand command, try again.")

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
        #print(newkey, message)
   
    for x in mess:
        cryptm.append(associations.find(x))
    for x in newkey:
        cryptk.append(associations.find(x))
    
    
    encrypt=[sum(x) for x in zip(cryptm, cryptk)]
    for x in encrypt:
        if x>85:
            encrypt=[(x-85) for x in encrypt]
        if x<0:
            encrypt=[(x+85) for x in encrypt]
    
#    for x in encrypt:
#       if x>85:
#            x.replace(x, x-85)
    
    
    for x in encrypt:
        tencrypt.append(associations[x])
    for x in tencrypt:
        print(x, end="")
    
    
if keystroke=="d":
    mess=input("Message:")
    key=input("Key:")
    k=len(key)
    m=len(mess)
    mes=[]
    cryptm=[]
    cryptk=[]
    decrypt=[]
    tdecrypt=[]
    
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
        
    
    
    decrypt=[x-y for x, y in zip(cryptm, cryptk)]
    for y in decrypt:
        if y>85:
            decrypt=[(y-85) for y in decrypt]
        if y<0:
            decrypt=[(y+85) for y in decrypt]
    
    
    for x in decrypt:
        tdecrypt.append(associations[x])
    for x in tdecrypt:
        print(x, end="")
        
    
if keystroke=="q":
    quit=True
    print("Goodbye!")
    





