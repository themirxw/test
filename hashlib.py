import hashlib
lam = 'salam'
my_hash =hashlib.sha1(lam.encode('utf-8'))
print(my_hash)