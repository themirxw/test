import random
import pandas as pd
import urllib.request

# Tabe baraye namayesh rangi matn
def colored(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

# Tarif mashin-haye Toyota
toyota = {
    "Model": ["Land Cruiser", "Camry", "Corolla", "RAV4", "Hilux", "Prius"], 
    "Price": [50000, 20000, 30000, 40000, 45000, 35000],  # Gheymatha be dollar
    "Year": [2024, 2020, 2023, 2022, 2019, 2018],
    "Description": [
        "Yek shasi boland ghavi ba ghabeliyatha-ye offroad ali.",
        "Yek sedan ghabel etminan ba masraf sukhte ali.",
        "Yek khodro-ye kuchak ke be khatere etebar va hazine negahdari kam mashhoor ast.",
        "Yek shasi boland chandkare monaseb baraye khanevadeha va majarajuyi.",
        "Yek pickup ghavi baraye kar va bazi.",
        "Yek khodro-ye hybrid doostdar mohite zist ba alayandeghi kam."
    ]
}

# Ejad DataFrame baraye namayesh behtar khodroha
Cars = pd.DataFrame(toyota)

# Mojoodi hesab ra dar inja tarif mikonim
mojoodi = 10000000  # 10 milion dollar
emtiaz = 0  # Emtiaz kharid

def menu():
    print(colored("-------- Menoye Asli --------", 'blue'))
    print("1. Kharid khodro Toyota")
    print("2. Moshahede mojoodi")
    print("3. Kharid va forosh Pride")
    print("4. Pishnahad khodro-ye vijhe")
    print("5. Namayesh khodro-haye lux")
    print("6. Khorooj")
    print(colored("----------------------------", 'blue'))

def kharid_khodro():
    print(Cars)
    # Gereftan voroodi az karbar baraye entekhab khodro
    while True:
        select_car = input(colored('Khodroy entekhabi khod ra vared konid: ', 'blue'))
        selected_model = select_car

        # Barresi vojood model dar DataFrame
        if selected_model in Cars['Model'].values:
            print(colored(f'{selected_model} ba movafaghiat entekhab shod :)', 'green'))
            break
        else:
            print(colored("Model vared shode dar list forosh mojood nist.", 'red'))
            print(colored("Lotfan dobare say konid.", 'yellow'))

    # Gereftan etelaat pardakht
    etebar_sanji = input(colored('Lotfan dobare model khodro ra vared konid: ', 'blue'))
    telephone = input(colored('Shomare khod ra vared konid: ', 'blue'))

    if etebar_sanji == selected_model:
        print(colored('Dar hal enteghal shoma be darghah pardakht...', 'green'))
    else:
        print(colored('Khodroy entekhabi eshtebah ast.', 'red'))
        return

    # Gereftan shomare kart va cvv2
    while True:
        card_number = input(colored('Lotfan shomare kart 16 raghami khod ra vared konid: ', 'blue'))
        if len(card_number) == 16 and card_number.isdigit():
            print(colored('Shomare kart motabar ast.', 'green'))
            cvv2 = input(colored('Lotfan cvv2 khod ra vared konid: ', 'blue'))
            break
        else:
            print(colored('Shomare kart namotabar ast. Lotfan dobare talash konid.', 'red'))

    # Tolid ramz tasadofi 5 raghami
    randnum = random.randint(10000, 99999)
    randnum = int(randnum)
    apiKavenegar = "https://api.kavenegar.com/v1/506F7A4F6A746A706A634D35687570596E4D7A6B2B4F765A594A4E4D64624A5552594C5945634A73704A633D/verify/lookup.json?receptor="+telephone+"&token="+str(randnum)+"&template=testolgo"
    import urllib.request
    contents = urllib.request.urlopen(apiKavenegar).read()

    # Gereftan ramz dovom az karbar
    ramz = int(input(colored('Lotfan ramz dovom ra vared konid: ', 'blue')))
    if ramz == randnum:
        print(colored('Pardakht ba movafaghiat anjam shod!', 'green'))
    
        # Peyda kardan gheymat khodroye entekhab shode
        car_price = Cars.loc[Cars['Model'] == selected_model, 'Price'].values[0]

        # Barresi mojoodi va kam kardan gheymat az mojoodi
        global mojoodi, emtiaz
        if mojoodi >= car_price:
            mojoodi -= car_price
            emtiaz += 1  # Afzayesh emtiaz kharid
            print(colored(f'Pardakht {car_price} dollar anjam shod.', 'green'))
            print(colored(f'Mojoodi baghi mande: {mojoodi} dollar.', 'green'))
            print(colored(f'Emtiaz kharid shoma: {emtiaz} emtiaz', 'yellow'))
        else:
            print(colored('Mojoodi kafi nist baraye pardakht.', 'red'))
    else:
        print(colored('Ramz vared shode eshtebah ast!!', 'red'))

def forosh_pride():
    pride_price = random.randint(1000, 5000)
    print(colored(f"Shoma mitavanid Pride khod ra ba gheymat {pride_price} dollar beforooshid.", 'green'))

    accept = input(colored("Aya mikhaid forosh anjam shavad? (yes/no): ", 'blue'))
    if accept.lower() == 'yes':
        global mojoodi
        mojoodi += pride_price
        print(colored(f'Forosh anjam shod. Mojoodi jadid: {mojoodi} dollar.', 'green'))
    else:
        print(colored('Forosh laghv shod.', 'red'))

def moshahede_mojoodi():
    print(colored(f'Mojoodi hesab: {mojoodi} dollar.', 'yellow'))

def pishnahad_khodro_vije():
    # Pishnahad tasadofi yek khodro az list ba takhfif
    random_car = random.choice(Cars['Model'].values)
    discount = random.randint(500, 3000)  # Takhfif tasadofi
    price_with_discount = Cars.loc[Cars['Model'] == random_car, 'Price'].values[0] - discount
    print(colored(f'Pishnahad vijhe: {random_car} ba takhfif {discount} dollar. Gheymat nahayi: {price_with_discount} dollar.', 'blue'))

def namayesh_khodro_lux():
    lux_cars = {
        "Model": ["Ferrari", "Lamborghini", "Rolls Royce"],
        "Price": [200000, 250000, 300000],
        "Year": [2022, 2021, 2023],
        "Description": [
            "Ferrari, shahkar sorat va tarahi italiayi.",
            "Lamborghini, ghovat va sabk manhaser be fard.",
            "Rolls Royce, namad lux boodan va rahat."
        ]
    }
    LuxCars = pd.DataFrame(lux_cars)
    print(colored("Khodro-haye lux mojood:", 'yellow'))
    print(LuxCars)

def main():
    while True:
        menu()
        choice = input(colored('Lotfan gozine morede nazar ra entekhab konid: ', 'blue'))

        if choice == '1':
            kharid_khodro()
        elif choice == '2':
            moshahede_mojoodi()
        elif choice == '3':
            forosh_pride()
        elif choice == '4':
            pishnahad_khodro_vije()
        elif choice == '5':
            namayesh_khodro_lux()
        elif choice == '6':
            print(colored('Khorooj az barname...', 'red'))
            break
        else:
            print(colored('Gozine eshtebah ast. Lotfan dobare talash konid.', 'red'))

# Shoroo barname
main()
