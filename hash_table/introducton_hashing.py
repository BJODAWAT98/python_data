import hashlib
# all available alogrithms in hashlib
hashlib.algorithms_guaranteed


md5_bojec = hashlib.md5()

md5_bojec.update

md5_bojec.update("bhavya jodawat")
md5_bojec.digest()


md5_bojec.block_size
##############################

# the size of the md5 is 16

import hashlib

crypt=hashlib.md5()
crypt.update(b"my name is bhavya jodawat")
print(crypt.digest())

print(crypt.digest_size)

###############################

# the size of sha256 is 32

import hashlib

crypt=hashlib.sha256()
crypt.update(b"my name is bhavya jodawat")
print(crypt.digest())

print(crypt.digest_size)

####################################


crypt=hashlib.md5()
crypt.update(b"hellow")
print(crypt.hexdigest())
