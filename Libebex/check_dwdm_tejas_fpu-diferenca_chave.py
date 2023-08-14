import os
from os import system
import string
from   bs4 import BeautifulSoup
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

UNKNOWN = -1
OK       = 0
WARNING  = 1
CRITICAL = 2

host  = sys.argv[1]
porta = sys.argv[2]
porta1 = sys.argv[3]

print(host)
print(porta)



url   = 'https://'+host+'/EMSRequest/Welcome'
body = {
    'session_key': 'DIAGUSER',
    'session_validation' : 'j72e#05t',
    'session_Domain' : '1',
    'session_send' : 'Submit'
}

session = requests.Session()
x = session.post(url, verify=False, data=body)
port_str = str(porta)  # Converte o número em uma string
port = [(digito) for digito in port_str] 

port_str1 = str(porta1)  # Converte o número em uma string
port1 = [(digito1) for digito1 in port_str1] 

dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
soup = BeautifulSoup(dataget.text, 'html.parser')
arraytd = [x.text for x in soup.find_all('td')]


dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port1[0]+''+port1[1]+''+port1[2]+'00'+port1[3]+'&RefreshRequest=False')
soup = BeautifulSoup(dataget.text, 'html.parser')
arraytd1 = [x.text for x in soup.find_all('td')]


fpu_trabalho = float(arraytd[2])
fpu_protecao = float(arraytd1[2])
print("dados")
print("Diferença")
diferenca= 6+fpu_trabalho-fpu_protecao
diffRx = int(diferenca)
print(diffRx)


if(diffRx <= 0 and diffRx <=-1 or diffRx >= 0 and diffRx <= 1 ):
    print("OK ")
   # print("OK ",sinalCorrente['rx'],"|'Rx'=",sinalCorrente['rx'],";-26;-40;-15,-25",sep="")
    exit(OK)
elif(diffRx <= 1 and diffRx <=-3 and diffRx >1 and diffRx < 3):
    print("WARNING ")
    
    exit(WARNING)

elif(diffRx <=-3 and diffRx >= 3):
    print("CRITICAL ")
    exit(CRITICAL)


