from Crypto.Cipher import AES
from Crypto import Random
"""
Using Python I see no reason to handcode every single bit of AES when it can come
in an easy to use library import.
Regardless, I still implemented the main portion of AES in PythonAES.py
This was just to show the main part about mixed columns and how some other features
are going to work.

This does encrypt a message with a specific key in Base64 10 times.
You can take out the while loop and encrpyt the message with the key once.
Or even specify a counter to encrypt the message.
"""
key = '0f1571c947d9e8591cb7add6af7f6798'

iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)

#Encrypt message once
#plainMessage = iv + cipher.encrypt('Hello World')

#Encrypts the message by a counter value, in this case by 10 and see each value it takes
count = 1
while (count<10):
	plainMessage = iv + cipher.encrypt('Hello World')
	print(plainMessage)
	count+=1

"""
#For the mix columns multiplications. Needs the GF to work with it since it will keep it 8 bits
#While also calculating the correct values in the columns
def GF(a,b):
	k = 0
	bit = 0
	for i in range(8):
		if b & 1==1:
			k^=a
		bit = a & 0x80
		a <<= 1
		if bit == 0x80:
			a ^=0x1b
		b >>= 1
	return k %256

def MixColumns(Col):
	column = copy(column)

	Col[0] = GF(column[0],2)^GF(column[3],1)^GF(column[2],1)^GF(column[1],3)
	Col[1] = GF(column[1],2)^GF(column[0],1)^GF(column[3],1)^GF(column[2],3)
	Col[2] = GF(column[2],2)^GF(column[1],1)^GF(column[0],1)^GF(column[3],3)
	Col[3] = GF(column[3],2)^GF(column[2],1)^GF(column[1],1)^GF(column[0],3)
"""