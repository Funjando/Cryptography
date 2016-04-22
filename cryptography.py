"""
cryptography.py
Author: Andreas Moberg
Credit: Payton (for mad math skillz), Ashwini Chauswerry, UncleZiev, Alejandro, Ethan

Assignment:

Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

infinity=1
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

#print(len(associations))
#85
while infinity>0:
    keystroke=input("Enter e to encrypt, d to decrypt, or q to quit: ")

    quit=False

    if keystroke not in ["e", "d", "q"]:
        print("Did not understand command, try again. ")

    if keystroke=="e":
        mess=input("Message: ")
        key=input("Key: ")
        k=len(key)
        m=len(mess)
        cryptm=[]
        cryptk=[]
        encrypt=[]
        tencrypt=[]
    
        if m>k:
            count=key*int((m-(m%k))/k)
            trun=key[0:(m%k)]
            key=count+trun
        elif k>m:
            key=key[0:m] 
            #print(newkey, message)
   
        for x in mess:
            cryptm.append(associations.find(x))
        for x in key:
            cryptk.append(associations.find(x))
    
    
        encrypt=[sum(x) for x in zip(cryptm, cryptk)]

    
#       for x in encrypt:
#           if x>85:
#               x.replace(x, x-85)
    
    
        for x in encrypt:
            tencrypt.append(associations[x%85])
        for x in tencrypt:
            print(x, end="")
        print("")
    
    
    if keystroke=="d":
        mess=input("Message: ")
        key=input("Key: ")
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
    
    
        for x in decrypt:
            tdecrypt.append(associations[x%85])
        for x in tdecrypt:
            print(x, end="")
        print("")
        
    
    if keystroke=="q":
        quit=True
        print("Goodbye!")
        infinity=infinity-1






