
from json import loads
from requests import get, post
from sys import exit

# USAGE:
# `pip install requests`
# `python3 ip.py`

# ONIONj :)

# free IP Geolocation
# get your free api key as https://ipstack.com/signup/free  10.000 requests / mo
# my api key:
TOKEN = 'ba8484c0c2706202049aa0bab48e9b9e'

banner = '''

████▄    ▄   ▄█ ████▄    ▄
█   █     █  ██ █   █     █
█   █ ██   █ ██ █   █ ██   █
▀████ █ █  █ ▐█ ▀████ █ █  █
      █  █ █  ▐ oNion █  █ █
      █   ██          █   ██ IP Geolocation
'''


def identify(target_ip):
    '''
    Target identification
    '''
    try:
        data = f'http://api.ipstack.com/{target_ip}?access_key={TOKEN}&format=1' 
        res = get(url = data)
        jtext = res.text
        jtext = loads(jtext)
        
        # data:
        ip = jtext['ip']
        city = jtext['city']
        ip_type = jtext['type']
        latitude = jtext['latitude']
        longitude = jtext['longitude']
        region_code = jtext['region_code']
        region_name = jtext['region_name']
        country_code = jtext['country_code']
        country_name = jtext['country_name']
        capital = jtext['location']['capital']
        continent_code = jtext['continent_code']
        continent_name = jtext['continent_name']
        calling_code = jtext['location']['calling_code']
        language_code = jtext['location']['languages'][0]['code']
        language_name = jtext['location']['languages'][0]['name']
        flag_pic = f'http://assets.ipstack.com/flags/{country_code.lower()}.svg'

        print(f'''
        ______________________
        |IP:                  {ip_type} {ip} 
        |Continent:           {continent_code} {continent_name}
        |Country:             {country_code} {country_name}
        |Region:              {region_code} {region_name}
        |City:                {city}
        |latitude:            {latitude}
        |longitude:           {longitude}
        |Capital:             {capital}
        |language:            {language_code} {language_name}
        |calling code:        {calling_code}
        |Flag photo link:     {flag_pic}
        -----------------------
        ''')
    except KeyboardInterrupt:
        print('[!] Exit by Ctrl+C')
        exit()
    except:
        print('[!] timeout !')


# Servers to get your public IP
def get_my_ip_server1():
    takeip = post("https://api.myip.com", timeout=3)    
    myipjson = takeip.text
    myip = str(loads(myipjson)["ip"])
    mycountry = str(loads(myipjson)["country"])
    ipaddr = "* IP Address : "+myip+"\n* country : "+mycountry+""
    return ipaddr

def get_my_ip_server2():
    myip = get('https://api.ipify.org', timeout=3).text
    ipaddr = f'* public IP address is: {myip}'
    return ipaddr

def get_my_ip_server3():
    myip = get('https://ident.me', timeout=3).text
    ipaddr = f'* public IP address is: {myip}'
    return ipaddr



def getmyip():
    '''
    return Your own public IP 
    '''
    ### try server 1
    try:
        return get_my_ip_server1()
    except KeyboardInterrupt:
        print('[!] Exit by Ctrl+C')
        exit()
    except:
        
        ### try server 2
        try:
            return get_my_ip_server2()
        except KeyboardInterrupt:
            print('[!] Exit by Ctrl+C')
            exit()
        except:

            ### try server 3
            try:
                return get_my_ip_server3()
            except KeyboardInterrupt:
                print('[!] Exit by Ctrl+C')
                exit()
            
            ### enough!
            except:
                print('[!] Three attempts from three different servers to get IP failed. Are you connected to the Internet?')
                return '0.0.0.0 the earth!'


if __name__ == '__main__':
    print(banner)
    # just print Your own public IP
    print(f'[+] youre ip:\n{getmyip()}\n')

    while True:
        # get target ip 
        try:
            target_ip = input(str('[>] IP Geolocation [IP or Q]\n>> '))

            if target_ip.lower() == 'q':
                print('[!] EXIT!')
                exit()
            else:
                # Target identification
                identify(target_ip)

        except KeyboardInterrupt:
            print('[!] Exit by Ctrl+C')
            exit()