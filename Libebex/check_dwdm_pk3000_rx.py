



from ast import arguments
from cmath import log
import sys
import requests
from bs4 import BeautifulSoup


arumentos = sys.argv
host = arumentos[1]
placa = int(arumentos[2])
rxRef = float(arumentos[3])

#10.1.55.138
ip0 = '10.1.55.1620' #Tiangua
ip1 = '10.1.55.162' #Tiangua
ip2 = '10.1.55.154' #Piripiri
ip3 = '10.1.55.146' #Campo Maior
ip4 = '10.1.55.138' #Teresina
ip5 = '10.1.60.42' # acailandia
ip6 = '10.1.60.50' # Imperatriz
ip7 = '10.1.60.2' # Santa InÊs
ip8 = '10.1.60.10' #santa luzia
ip9 = '10.1.60.18' #Santo onofre
ip10 = '10.1.60.26' #Buriticypu-2
ip11 = '10.1.60.34' #Bom Jesus
OK       = 0
WARNING  = 1
CRITICAL = 2

url = 'http://'+host+':8081/fast/php/mcSysLogin/login.php'
body = {
    "id": "0",
    "name": "0",
    "data": {
      "account": "admin",
      "password": "admin",
      "captcha": ""
    }
  }
response = requests.get('http://'+host+':8081/fast/php/mcCardMonitor/findMonitor.php')
response.raise_for_status()
jsonResponse = response.json()

currentRx=jsonResponse["data"]["cardData"][placa-1]["da"][1]


result=float(currentRx)

rx = result

diffRx = abs(rx-rxRef)


if(diffRx >= 0 and diffRx <= 1):
      #print("OK ",result['rx'],"|'Rx'=",result['rx'],";-26;-40;-15,-25",sep="")
      print("OK ",result,"|'Rx'=",result,";-26;-40;-15,-25",sep="")
      exit(OK)
if(diffRx >1 and diffRx < 3):
      #print("WARNING ",result['rx'],"|'Rx'=",result['rx'],";-26;-40;-15,-25",sep="")
       print("WARNING ",result,"|'Rx'=",result,";-26;-40;-15,-25",sep="")
       exit(WARNING)
if(diffRx >= 3):
      #print("CRITICAL ",result['rx'],"|'Rx'=",result['rx'],";-26;-40;-15,-25",sep="")
       print("CRITICAL ",result,"|'Rx'=",result,";-26;-40;-15,-25",sep="")
       exit(CRITICAL)


