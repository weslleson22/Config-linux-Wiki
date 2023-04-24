from ast import arguments
from cmath import log
import sys
import requests
from bs4 import BeautifulSoup

UNKNOWN  = -1
OK       = 0
WARNING  = 1
CRITICAL = 2

arumentos = sys.argv
host = arumentos[1]
placa = int(arumentos[2])
mode = int(arumentos[3])
rxRef = float(arumentos[4])


ip3 = '10.1.55.146' #Campo Maior
ip4 = '10.1.55.138' #Teresina
ip6 = '10.1.60.50' # Imperatriz
ip7 = '10.1.60.2' # Santa InÊs
ip8 = '10.1.55.154' #piriripi



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

  
if (mode == 0):
    ## Pegar o sinal da TX da Placa
    current=jsonResponse["data"]["cardData"][placa-1]["da"][10]
if(mode == 1):
    ## Pegar o sinal da R1 da Placa
    current=jsonResponse["data"]["cardData"][placa-1]["da"][8]
if(mode == 2):
    ## Pegar o sinal da R2 da Placa
    current=jsonResponse["data"]["cardData"][placa-1]["da"][9]


result=float(current)

rx = result

diffRx = abs(rx-rxRef)


if(diffRx >= 0 and diffRx <= 1):
      #print("OK ",result['rx'],"|'Rx'=",result['rx'],";-26;-40;-15,-25",sep="")
      print("OK ",result,"|'Tx'=",result,";-26;-40;-15,-25",sep="")
      exit(OK)

if(diffRx >1 and diffRx < 3):
      #print("WARNING ",result['rx'],"|'Rx'=",result['rx'],";-26;-40;-15,-25",sep="")
       print("WARNING ",result,"|'Tx'=",result,";-26;-40;-15,-25",sep="")
       exit(WARNING)

if(diffRx >= 3):
      #print("CRITICAL ",result['rx'],"|'Rx'=",result['rx'],";-26;-40;-15,-25",sep="")
       print("CRITICAL ",result,"|'Tx'=",result,";-26;-40;-15,-25",sep="")
       exit(CRITICAL)






