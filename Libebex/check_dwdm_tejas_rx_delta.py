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
        'Rx':rxRef,
    }

    diffRx = calcRx(sinalCorrente['rx'],sinalReferencia['Rx'])
    # diffRx = 20
   
    if(diffRx >= 0 ):
        print('Ganho de  {:.2f}'.format(diffRx),"|'Delta'=",'{:.2f}'.format(diffRx),";-26;-40;-15,-25",sep="")
        exit(OK)

    if(diffRx <0):
        print('Atenuação de  {:.2f}'.format(diffRx),"|'Delta'=",'{:.2f}'.format(diffRx),";-26;-40;-15,-25",sep="")
        exit(WARNING)


def calcRx(rxRef, currentRx):
    result = float(rxRef)-float(currentRx)
  
    return (round(result,4))


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
    ip7= '10.1.55.210' #Sobral
    ip8= '10.1.55.50' #chapadinha
    ip9= '10.1.55.58' #brejo
    if(host == ip2) and (porta == '131') or (host == ip3) and (porta == '141'):
        rx = arraytd[11].replace(" ","")
    elif(host == ip4) and (porta == '1702') or (host == ip4) and (porta == '1703'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        rx = arraytd[3].replace(" ","")

    elif(host == ip5) and (porta == '1362') or (host == ip5) and (porta == '1363') or (host == ip5) and (porta == '1352') or (host == ip5) and (porta == '1353'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        rx = arraytd[3].replace(" ","")

    elif(host == ip6) and (porta == '1362') or (host == ip6) and (porta == '1363') or (host == ip6) and (porta == '1352') or (host == ip6) and (porta == '1353'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        rx = arraytd[3].replace(" ","")
    elif(host == ip7) and (porta == '1352') or (host == ip7) and (porta == '1353'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        rx = arraytd[3].replace(" ","")

    elif(host == ip8) and (porta == '1752') or (host == ip8) and (porta == '1753'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        rx = arraytd[2].replace(" ","")

    elif(host == ip9) and (porta == '1352') or (host == ip9) and (porta == '1353'):

        dataget  = session.get('https://'+host+'/EMSRequest/perfCurrent?Interface=FPU&IfNum='+port[0]+''+port[1]+''+port[2]+'00'+port[3]+'&RefreshRequest=False')
        soup    = BeautifulSoup(dataget.text, 'html.parser')
        arraytd = [x.text
        for x in soup.find_all('td')]
        rx = arraytd[2].replace(" ","")


    else:
        (host == ip2) and (porta != '131') or (host == ip3) and (porta != '141')

        rx = arraytd[9].replace(" ","")
    #print(arraytd)
   # tx      = arraytd[10]

    return  {
        'rx':rx,
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



UNKNOWN = -1
OK       = 0
WARNING  = 1
CRITICAL = 2

host  = sys.argv[1]
porta = sys.argv[2]
rxRef = sys.argv[3]
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














































































































































































































