import hashlib
import random
import urllib.request
file_path = 'text_file.txt'
with open(file_path, 'w') as file:
    cart = {
        "shomare_kart": "6037554585038503",
        "cvv2": 357,
        "engheza": "04/01"
    }
    if cart["shomare_kart"] == input("6037554585038503:"):
        file.write('shomare kart dorostbode\n')
        print('doroste')
        if cart["cvv2"] == int(input('cvv2 ra vared konid:')):
            file.write('cvv2 dorostbode\n')
            print('doroste')
            if cart["engheza"] == input('04/01:'):
                file.write('tarikh engheza kart dorostbode\n')
                print('doroste')
            else:
                file.write('nadoroste bode tarikh enghezash\n')
                print('nadoroste')
        else:
            file.write('nadorost bode cvv2  \n')
            print('nadoroste')
    else:
        file.write('nadorost shomare kart\n')
        print('nadoroste')
    telephone = input('shomare khod ra vared konid:')
    file.write(f'shomare khod: {telephone}\n')
    randnum = ''
    for _ in range(5):
        randnum += str(random.randint(0, 9))
    hash_object = hashlib.sha1(randnum.encode())
    hash = hash_object.hexdigest()
    print(hash)
    file.write(f'hash: {hash}\n')
    apiKavenegar = "https://api.kavenegar.com/v1/506F7A4F6A746A706A634D35687570596E4D7A6B2B4F765A594A4E4D64624A5552594C5945634A73704A633D/verify/lookup.json?receptor=" + telephone + "&token=" + str(randnum) + "&template=testolgo"
    contents = urllib.request.urlopen(apiKavenegar).read()
    ramz = input('ramz khod ra vared konid(5 raghami bala:).....):')
    file.write(f'ramz vared shode: {ramz}\n')
    hash_varede = hashlib.sha1(ramz.encode())
    hash1 = hash_varede.hexdigest()
    if hash1 == hash: 
        file.write('khosh amadid\n')
        print('khosh amadid')
        mablagh = 200000
        adad = int(input('variz vajhe adad 1 ra bezanid va baray bardasht vajhe adad 2 ra bezanid:'))
        file.write(f'adad vared shode (adad 1 = variz vajhe , adad 2 = bardasht vajhe): {adad}\n')

        if adad == 1:
            variz = int(input('mablagh ra vared konid:'))
            file.write(f'variz: {variz}\n')
            mojodi = mablagh + variz
            print('mojodi jadid:', mojodi)
            file.write(f'mojodi jadid: {mojodi}\n')

        elif adad == 2:
            bardasht = int(input('mablagh ra vared konid:'))
            file.write(f'bardasht: {bardasht}\n')
            mojodi = mablagh - bardasht
            print('mojodi jadid:', mojodi, "T")
            file.write(f'mojodi jadid: {mojodi} T\n')

        else:
            print('adad vared shode eshtebah ast')
            file.write('adad vared shode eshtebah ast\n')

    else:
        print("nadorost ast va chand daghighe bad talash konid")
        file.write("nadorost ast va chand daghighe bad talash konid\n")

print("file text shoma zakhire shod ")




code = '''
import hashlib
import random
import urllib.request
file_path = 'text_file.txt'
with open(file_path, 'w') as file:
    cart = {
        "shomare_kart": "6037554585038503",
        "cvv2": 357,
        "engheza": "04/01"
    }
    if cart["shomare_kart"] == input("6037554585038503:"):
        file.write('shomare kart dorostbode\\n')
        print('doroste')
        if cart["cvv2"] == int(input('cvv2 ra vared konid:')):
            file.write('cvv2 dorostbode\\n')
            print('doroste')
            if cart["engheza"] == input('04/01:'):
                file.write('tarikh engheza kart dorostbode\\n')
                print('doroste')
            else:
                file.write('nadoroste bode tarikh enghezash\\n')
                print('nadoroste')
        else:
            file.write('nadorost bode cvv2\\n')
            print('nadoroste')
    else:
        file.write('nadorost shomare kart\\n')
        print('nadoroste')
    telephone = input('shomare khod ra vared konid:')
    file.write(f'shomare khod: {telephone}\\n')
    randnum = ''
    for _ in range(5):
        randnum += str(random.randint(0, 9))
    hash_object = hashlib.sha1(randnum.encode())
    hash = hash_object.hexdigest()
    print(hash)
    file.write(f'hash: {hash}\\n')
    apiKavenegar = "https://api.kavenegar.com/v1/506F7A4F6A746A706A634D35687570596E4D7A6B2B4F765A594A4E4D64624A5552594C5945634A73704A633D/verify/lookup.json?receptor=" + telephone + "&token=" + str(randnum) + "&template=testolgo"
    contents = urllib.request.urlopen(apiKavenegar).read()
    ramz = input('ramz khod ra vared konid(5 raghami bala:).....):')
    file.write(f'ramz vared shode: {ramz}\\n')
    hash_varede = hashlib.sha1(ramz.encode())
    hash1 = hash_varede.hexdigest()
    if hash1 == hash:
        file.write('khosh amadid\\n')
        print('khosh amadid')
        mablagh = 200000
        adad = int(input('variz vajhe adad 1 ra bezanid va baray bardasht vajhe adad 2 ra bezanid:'))
        file.write(f'adad vared shode (adad 1 = variz vajhe , adad 2 = bardasht vajhe): {adad}\\n')

        if adad == 1:
            variz = int(input('mablagh ra vared konid:'))
            file.write(f'variz: {variz}\\n')
            mojodi = mablagh + variz
            print('mojodi jadid:', mojodi)
            file.write(f'mojodi jadid: {mojodi}\\n')

        elif adad == 2:
            bardasht = int(input('mablagh ra vared konid:'))
            file.write(f'bardasht: {bardasht}\\n')
            mojodi = mablagh - bardasht
            print('mojodi jadid:', mojodi, "T")
            file.write(f'mojodi jadid: {mojodi} T\\n')

        else:
            print('adad vared shode eshtebah ast')
            file.write('adad vared shode eshtebah ast\\n')

    else:
        print("nadorost ast va chand daghighe bad talash konid")
        file.write("nadorost ast va chand daghighe bad talash konid\\n")

print("file text shoma zakhire shod ")
'''

with open('code_file.txt', 'w') as file:
    file.write(code)
