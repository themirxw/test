import hashlib
cart = {
    "shomare_kart": "6037554585038503",
    "cvv2": 357,
    "engheza": "04/01"}
if cart["shomare_kart"] == input("6037554585038503:"):
    print('doroste')
    if cart ["cvv2"] == input('cvv2 ra vared konid:'):
        print('doroste')
        if cart["engheza"] == input('04/01:'):
             print('doroste')
else:
    print('nadoroste')
telephone = input('shomare khod ra vared konid:')
import random
randnum = ''
for _ in range(5):
    randnum += str(random.randint(0, 9))
hash_object = hashlib.sha1(randnum.encode())
hash = hash_object.hexdigest()
print(hash)
apiKavenegar = "https://api.kavenegar.com/v1/506F7A4F6A746A706A634D35687570596E4D7A6B2B4F765A594A4E4D64624A5552594C5945634A73704A633D/verify/lookup.json?receptor="+telephone+"&token="+str(randnum)+"&template=testolgo"
import urllib.request
contents = urllib.request.urlopen(apiKavenegar).read()
ramz = input('ramz khod ra vared konid(5 raghami bala:).....):')
hash_varede = hashlib.sha1(ramz.encode())
hash1 = hash_varede.hexdigest()
if hash1 == hash: 
    print ('khosh amadid')
    mablagh = 200000
    adad = int(input('variz vajhe adad 1 ra bezanid va baray bardasht vajhe adad 2 ra bezanid:'))
    if adad == 1:
        variz = int(input('mablagh ra vared konid:'))
        mojodi = mablagh + variz
        print('mojodi jadid:', mojodi)
    elif adad == 2:
        bardasht = int(input('mablagh ra vared konid:'))
        mojodi = mablagh - bardasht
        print('mojodi jadid:', mojodi , "T")
    else:
        print('adad vared shode eshtebah ast')
else:
    print ("nadorost ast va chand daghighe bad talash konid")
    #با فایل تکست ذخیره بشه به صورت هش شده و هش باید با هش مقایسه شود
    #رمز بشه عوض بشه تو فایل تکست ذخیره بشه
