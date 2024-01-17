from pysnmp.hlapi import *

ipaddr = '10.31.70.209'
community_name = 'public'
port_int = '161'
snmp_name = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result_1 = getCmd(
    SnmpEngine(),
    CommunityData(community_name, mpModel=0),
    UdpTransportTarget((ipaddr, port_int)),
    ContextData(),
    ObjectType(snmp_name)
)
for i in result_1:
#    print(i)
    for j in i[3]:
        print(j)


result_2 = nextCmd(
    SnmpEngine(),
    CommunityData(community_name, mpModel=0),
    UdpTransportTarget((ipaddr, port_int)),
    ContextData(),
    ObjectType(snmp_object),
    lexicographicMode=False
)
for k in result_2:
#    print(k)
    for l in k[3]:
        print(l)