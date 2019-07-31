'''
Author : SANJAY KUMAR PS
Ver    : 0.1
Date   : 31st Jul'19
A program that gives the count of number of entries in each link state in the OSPF database
The input to be the output of 'show ip ospf database' table assigned to 'text'
'''

text= ''  #show ip ospf database output

i=0
temp=''
for line in text.splitlines():
    if len(line) == 0:
        continue
    if 'Link States' in line:
        print(temp+' '+str(i-1))
        temp=line
        i=0
        continue
    i=i+1
print(temp+' '+str(i))
