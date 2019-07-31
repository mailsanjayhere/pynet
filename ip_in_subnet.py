import ipaddress
'''
This program is to find if an IP is part of a pool.
List of hosts are listed under the list iplist
List of subnets are listed under subnetlist
The output will be printed as to which address is part of the list and which not
'''

iplist=['10.203.248.165','10.203.248.99','10.203.248.100','10.203.248.103','10.205.89.99','10.205.89.100','10.205.89.103']
subnetlist=['10.43.24.64/26','10.43.28.64/26','10.203.248.0/26','10.203.248.64/26','10.203.248.128/26','10.203.248.192/26']

for ip in iplist:
    i=0
    ip=ip+'/32'
    ip=ipaddress.ip_network(ip)
    for net in subnetlist:
        if ip.subnet_of(ipaddress.ip_network(net)):
            i=1
            continue
    if i == 0:
        print(str(ip)+' not in the list')
    else:
        print(str(ip)+' is in the list')
    i=0
