import hashlib

for i in range(1,9999999):
    if(hashlib.md5(str(i).encode("utf8")).hexdigest()[0:6]=='847cc5' and hashlib.md5(str(i).encode("utf8")).hexdigest()[-4:]== 'a8a5'):
        print(i)
