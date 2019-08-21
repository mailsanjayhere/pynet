'''
Author: SANJAY KUMAR P S
Version 0.1
Date: 21st Aug 2019

Below file builds the configuration for the routers
template should be an excel file
that has two sheets
The first sheet contains
Device1 Device2 Inf1  inf2

The second sheet contains two columns
First column the ip networks for IRLs
and the 
second column has ip addresses for loopbacks
'''

import xlrd
from xlrd import open_workbook,cellname
from ipaddress import IPv4Network




book = open_workbook('example.xlsx')
sheet1 = book.sheet_by_index(0)

dev_inf={}
for i in range(1,sheet1.nrows):  #1 is to exclude the first row
    dev_inf[(sheet1.cell(i,0).value,sheet1.cell(i,1).value)] = ((sheet1.cell(i,2).value),sheet1.cell(i,3).value)
print(dev_inf)

device_list = []
for k in dev_inf.keys():
    device_list.append(k[0])
    device_list.append(k[1])



irl_list=[]
loopback=[]
sheet2 = book.sheet_by_index(1)


for i in range(sheet2.nrows):
    irl_list.append(sheet2.cell(i,0).value)
    loopback.append(sheet2.cell(i,1).value)


device_list = list(set(device_list))
i=0
for device in device_list:
    with open(device+'.txt','w') as f:
        f.write('''
hostname {}
int lo0
 ip address {} 255.255.255.255\n'''.format(device,loopback[i]))
        i=i+1


print(device_list)

i=0

for k,v in dev_inf.items():
    cfg1 = '''
int {}
 no shutdown
 ip address {} 255.255.255.252
 description {}
    '''.format(v[0],IPv4Network((irl_list[i])+'/30')[1],k[1])
    cfg2 = '''
int {}
 no shutdown
 ip address {} 255.255.255.252
 description {}
    '''.format(v[1],IPv4Network((irl_list[i])+'/30')[2],k[0])
    with open(k[0]+'.txt','at') as f:
        f.write(cfg1)
    with open(k[1]+'.txt','at') as f:
        f.write(cfg2)
    i=i+1
