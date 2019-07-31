import os
import pprint
'''
Author : SANJAY KUMAR PS
Ver    : 0.1
Date   : 31st Jul 2019
Below program creates the dictironary of device names as keys and (sbunet,attached interface) as their values
Basically the connected subnets for a device is listed
The input to this program is the folder that contains the files with names as the device hostnames and has the contents of 
show ip route connected -> in case of IOS
show ip route local -> in case of NX-OS
'''
os.chdir('c:\Python3')  #The respective path where the files of show ip route connected/local is available
files= os.listdir()
rt={}
i=0
for device in files:
    sub=[] #subnets
    with open(device,'rt') as f:
        routes = f.read()
    d_name = device.replace('.txt', '')
    if 'Could not resolve "connected"' in routes:
        for line in routes.splitlines():
            if 'attached' and 'ubest' in line:
                temp1 = line.split()[0].replace(',','')
                i=0
            elif 'local' and 'via' in line:
                temp2 = line.split()[2].replace(',','')
                i=1
            if i == 1:
                sub.append((temp1,temp2))
                i=0
        rt[d_name] = sub
        sub=[]
    else:
        for line in routes.splitlines():
            if 'directly connected' in line:
                sub.append((line.split()[1],line.split()[-1]))
        rt[d_name] = sub
        sub=[]

pprint.pprint(rt)
