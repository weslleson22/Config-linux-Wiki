import os
from os import system
import string
from   bs4 import BeautifulSoup
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def Main():
    sinalCorrente = getData(host=host,porta=porta)
    sinalReferencia = {
        'Tx':TxRef,
    }

    diffTx = calcTx(sinalCorrente['Tx'],sinalReferencia['Tx'])
    # diffTx = 20

    if(diffTx >= 0 and diffTx <= 1):
        print("OK ",sinalCorrente['Tx'],"|'Tx'=",sinalCorrente['Tx'],";-26;-40;-15,-25",sep="")
        exit(OK)

    if(diffTx >1 and diffTx < 3):
        print("WARNING ",sinalCorrente['Tx'],"|'Tx'=",sinalCorrente['Tx'],";-26;-40;-15,-25",sep="")
        exit(WARNING)

    if(diffTx >= 3):
        print("CRITICAL ",sinalCorrente['Tx'],"|'Tx'=",sinalCorrente['Tx'],";-26;-40;-15,-25",sep="")
        exit(CRITICAL)


def calcTx(TxRef, currentTx):
    result = float(TxRef)-float(currentTx)
    return abs(round(result,4))

def getData(host, porta):
    port    = list(porta)
   ## print(port)
  ##  print(host)
   # ip=host

   ##    print("Mais um vetor")
     #   x=1


    portType= convertPort(port=port)
    bdata   = getBodyUrl(checkHost(host=host))
    session = requests.Session()
    x       = session.post(url, verify=False, data=bdata)


    #print(portType)
    if(portType == 0):
        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=OFA&IfNum='+port[0]+'0'+port[1]+'00'+port[2]+'&RefreshRequest=False')
    if(portType == 1):
        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=OFA&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')

    soup    = BeautifulSoup(dataget.text, 'html.parser')
    arraytd = [x.text
    for x in soup.find_all('td')]

    ip2 ='10.1.55.18'
    ip3 ='10.1.55.2'
    ip4 = '10.1.55.122'
    ip5= '10.1.55.134'#Croata
    ip6= '10.1.55.114'#Itapage
    ip7= '10.1.55.210'#Sobral




    if(host == ip2) and (porta == '131') or (host == ip3) and (porta == '141'):
        Tx = arraytd[12].replace(" ","")
    elif(host == ip4) and (porta == '1702') or (host == ip4) and (porta == '1703'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        Tx = arraytd[4].replace(" ","")

    elif(host == ip5) and (porta == '1362') or (host == ip5) and (porta == '1363') or (host == ip5) and (porta == '1352') or (host == ip5) and (porta == '1353'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        Tx = arraytd[4].replace(" ","")

    elif(host == ip6) and (porta == '1362') or (host == ip6) and (porta == '1363') or (host == ip6) and (porta == '1352') or (host == ip6) and (porta == '1353'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        Tx = arraytd[4].replace(" ","")
    elif(host == ip7) and (porta == '1352') or (host == ip7) and (porta == '1353'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        Tx = arraytd[3].replace(" ","")

    else:
        (host == ip2) and (porta != '131') or (host == ip3) and (porta != '141')

        Tx = arraytd[10].replace(" ","")
    #print(arraytd)
   # tx      = arraytd[10]

    return  {
        'Tx':Tx,
    }

def checkHost(host):
    try:
        rst = rotaItz.index(host)
        rst = True
    except:
        rst = False

    return rst

def getBodyUrl(type):
    if(type):
        body = {
            'Username'        : 'DIAGUSER',
            'Password'        : 'j72e#05t',
            'Domain'          : '1',
            'Submit'          : 'Submit'
        }
    else:
        body = {
            'session_key'        : 'DIAGUSER',
            'session_validation' : 'j72e#05t',
            'session_Domain'     : '1',
            'session_send'       : 'Submit'
        }
    return body

def convertPort(port):
    if(len(port) == 3):
        portType = 0
    else:
        portType = 1
    return portType


UNKNOWN  = -1
OK       = 0
WARNING  = 1
CRITICAL = 2

host  = sys.argv[1]
porta = sys.argv[2]
TxRef = sys.argv[3]
portType = 0
rotaItz = ['10.1.55.2', #OK
           '10.1.55.18', #OK
           '10.1.55.26', #UNK
           '10.1.55.34', #UNK
           '10.1.55.42', #OK
           '10.1.55.250'] #OK


url   = 'https://'+host+'/EMSRequest/Welcome'
system("title Tejas Plugin by WY")
Main()



