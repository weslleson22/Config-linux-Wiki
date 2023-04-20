
#!/usr/bin/python
import os
import sys

args1=sys.argv[1]
args2=sys.argv[2]

o=os.popen('/usr/local/nagios/libexec/check_snmp -H %s -C w1k1rty123 -P 2c -o SNMPv2-SMI::enterprises.2011.5.25.31.1.1.3.1.8.%s' %(args1,args2)).read()
#print(o)
sinal=o[10:15]
#print sinal
sinal = float(sinal)/1000*10


#sinal=-26.9
#print sinal

if sinal == -40:
        print ("CRITICAL  %s | 'Rx'=%s;-26;-40;-15,-25" %(sinal,sinal))
        sys.exit(2)

elif sinal >= -26:
        print ("OK  %s | 'Rx'=%s;-26;-40;-15,-25" %(sinal,sinal))
        sys.exit(0)

elif sinal <= -26:
        print ("WARNING  %s | 'Rx'=%s;-26;-40;-15,-25" %(sinal,sinal))
        sys.exit(1)

else:
        print ("UNKNOWN  %s Desconhecido | 'Rx'=%s;-26;-40;-15,-25" %(sinal,sinal))
        sys.exit(3)


