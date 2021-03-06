import httplib2
import serial
import requests
import time

from twilio.rest import Client

account = "__account id__"

token = "__token id__"

client = Client(account, token)

ser=serial.Serial('COM3',9600,timeout=2)
while (True):
    i=0
    t=[0,0,0,0]
    while(i<6):
        ch=(ser.readline().strip())
        r=str(ch).split('$')
        if len(r)==6:
            r=[float(r[i]) for i in range(1,5)]
            t[0]+=r[0]
            t[1]+=r[1]
            t[2]+=r[2]
            t[3]+=r[3]
            i+=1
    else:
        t=[y/6.0 for y in t]
        msg=""
        if t[0]>90:
            msg="High level of Humidity in your Area"
        elif t[0]<20:
            msg="Low level of Humidity in your Area"
        elif t[1]>45:
            msg="High Temperature (above 45 deg Cel) in your Area"
        elif t[1]<10:
            msg="Low Temperature (below 10 deg Cel) in your Area"
        elif t[2]>600:
            msg="The Air in your Area is polluted"
        elif t[2]>1000:
            msg="The Air in your Area is highly polluted"
            
        if msg!="":
            print("---->>>message")
            message = client.messages.create(to="__ur phone number__", from_="__twilio virtual number__",body=msg)
        print(t)        
        t1=requests.get("https://api.thingspeak.com/update?api_key=__channel id__&field1=%s"%(t[1]))
        t2=requests.get("https://api.thingspeak.com/update?api_key=__channel id__&field2=%s"%(t[0]))
        t3=requests.get("https://api.thingspeak.com/update?api_key=__channel id__&field3=%s"%(t[2]))
        t4=requests.get("https://api.thingspeak.com/update?api_key=__channel id__&field4=%s"%(t[3]))
        
       
        print(t4,t3,t2,t1)
        print("Uploaded")
        
