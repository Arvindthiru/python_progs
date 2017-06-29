
def encrypt(plain,shift):
	cipher=""
	plain=plain.lower()
	for i in plain:
		i=(ord(i)+3)%122
		if(i<97):
			i=i+96
		cipher=cipher+chr(i)
	return cipher

plain=raw_input()
str=encrypt(plain,3)
print str
