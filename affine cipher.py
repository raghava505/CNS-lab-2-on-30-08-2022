#!/usr/bin/env python
# coding: utf-8

# In[36]:


a,b = list(map(int,input("Enter the values of a and b (space seperated)").split(" ")))
message = input("enter the message")


# In[37]:


print(a,b)
message = message.upper()
print(message)


# In[48]:


import math

def mul_inv():
    if math.gcd(a,26) ==1 :
        for i in range(0,26):
            if (i*a) % 26 == 1:
                return i
    else:
        return 100

def encrypt():
    ans=[]
    for i in message:
        ans.append(chr( ((((ord(i)-65)*a)+b)%26)+65  ))
        
    return ans


def decrypt(enc):
    ans=[]
    a_inv = mul_inv()
    for i in enc:
        ans.append(chr(((((ord(i)-65-b +26)%26)*a_inv)%26)+65))
    return ans
    

    
    
a_inv = mul_inv()
print("multiplicative inverse of a is : ", a_inv)
if a_inv ==100 :
    print("Sorry ,cannot please try another encryption method ")
else:
    enc = ''.join(encrypt())
    print("The encrypted messgae is :" , enc)
    print("Message after decryption : " , ''.join(decrypt(enc)))


# In[46]:





# In[ ]:




