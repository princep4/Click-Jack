from colorama.ansi import Back, Fore, Style
import requests
import sys
from colorama import Fore, Back, Style

var2xx=['200','201','202','203']
var3xx=['300','301','302','303']
var4xx=['400','401','402','403','404']

print(Fore.RED,'''

  ____ _     ___ ____ _  __            _            _    
 / ___| |   |_ _/ ___| |/ /           (_) __ _  ___| | __
| |   | |    | | |   | ' /   _____    | |/ _` |/ __| |/ /
| |___| |___ | | |___| . \  |_____|   | | (_| | (__|   < 
 \____|_____|___\____|_|\_\          _/ |\__,_|\___|_|\_\/
                                    |__/                    
                            
                    ''',Fore.YELLOW,'''        By: Prince Prafull ''',Fore.BLUE,'''
    Support:-
            {+} Twitter: PrincePrafull3
            {+} Github : princep4 
            {+} BTC Wallet: 3QuqxhoRaksYKyiQDCvBiJkeSrz4eECkxy

''',Fore.YELLOW,'''################################## Lets \U0001f600 START ################################## 
  ''')

file1 = open(sys.argv[1], 'r')
urls = file1.read().splitlines()
#print(urls)
for url in urls:
    try:
        response = requests.get(url,timeout=5)
        status=str(response.status_code)
        #print(status)
        if status in var2xx:
            if (("X-Frame-Options" not in response.headers) or ("x-frame-options" not in response.headers)):
                print(Fore.RED, url,' is ',' VULNERABLE ')
                file=open('url_with_clickjacking.txt','a')
                file.write(url)
                file.write("\n")
            else:
                print(Fore.GREEN, url,' is ',' NOT VULNERABLE ')
        else:
            Exception
    except Exception:
        print(Fore.WHITE,"Error To Browse URL: ",url)

print("\n\n",Fore.YELLOW,"The Vulnerable URLs are saved to url_with_clickjacking.txt")      
file.close()



