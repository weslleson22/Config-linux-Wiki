import os
from   bs4 import BeautifulSoup
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)





UNKNOWN  = -1
OK       = 0
WARNING  = 1
CRITICAL = 2

host  = sys.argv[1]
porta = sys.argv[2]

url   = 'https://'+host+'/EMSRequest/Welcome'

body = {
    'session_key'        : 'DIAGUSER',
    'session_validation' : 'j72e#05t',
    'session_Domain'     : '1',
    'session_send'       : 'Submit'
}

#  ip5= '10.1.55.134'#Croata
#   ip6= '10.1.55.114'#Itapage 

session = requests.Session()
x       = session.post(url, verify=False, data=body)

dataget = session.get('https://'+host+'/EMSRequest/tic?Slot='+porta+'&Shelf=1')
soup = BeautifulSoup(dataget.text, 'html.parser')
arraytd = [x.text for x in soup.find_all('th')]


if(arraytd[13] == 'Work '):
    print("OK - ATIVA WORK")
    exit(OK)

elif(arraytd[13] == 'Protect '):
    print("WARNING - ATIVA PROTECT")
    exit(WARNING)

elif(arraytd[13] != 'Work' and arraytd[13] != 'Protect'):
    print("CRITICAL")
    exit(CRITICAL)
