from ast import In
from colorama.ansi import Back, Fore, Style
import requests
import sys
from colorama import Fore, Back, Style
from sympy import arg

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


def findClickJack(urls):
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
                    file.close()
                else:
                    print(Fore.GREEN, url,' is ',' NOT VULNERABLE ')
            else:
                pass

        except Exception as e:
            print(Fore.WHITE,"Error To Browse URL: ",url,e)
            break
    else:
        print("\n\n",Fore.YELLOW,"The Vulnerable URLs are saved to url_with_clickjacking.txt")    


def main():
    # using argparse:
############################################
    urlist=[]
    import argparse
    parser = argparse.ArgumentParser(description='Click Jack')
    parser.add_argument('-url', dest='url', nargs="+" ,help='List of URLs')
    parser.add_argument('-file', dest='file', type=str, help='Filename containing URL(s) ')
    args = parser.parse_args()

    if args.url:
        findClickJack(args.url)
    elif args.file:
        
        try:
            file1 = open(args.file, 'r')
            urlist = file1.read().splitlines()
            findClickJack(urlist)
        except OSError as e:
            print("Error in reading file.",e)
    else:
        print("No URL(s) or file argument found.")
###########################################
  
    # using sys.args:
############################################
    
    # if (len(sys.argv)==2):
    #     try:
    #         file1 = open(sys.argv[1], 'r')
    #         urlist = file1.read().splitlines()
    #         findClickJack(urlist)
    #     except OSError as e:
    #         if e.errno == 22:
    #             urlist.append(sys.argv[1])
    #             findClickJack(urlist)
    #         else:
    #             print(e)
    # elif(len(sys.argv)>2):
    #     for i in range(1, len(sys.argv)):
            
    #         urlist.append(sys.argv[i])
        
    #     findClickJack(urlist)
    # else:
    #     print("No URL(s) or file argument found.")

############################################


if __name__ == "__main__":
    main()