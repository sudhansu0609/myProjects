import ipaddress as ip
from math import floor, remainder
import RequestsLibrary

from RequestsLibrary import RequestsKeywords
import requests.sessions
import certifi
from OpenSSL.crypto import verify

#from scripts.VersionStamp.vssutil import SubstituteInString


# 
# class Calculate_And_Validate_Ip(object):
#     def __init__(self):
#        pass
def get_ipv4_ip_range(self,address,cidr):
    IP_range=address+ r'/'+ cidr
    ip_range = ip.ip_network(IP_range,strict=False)
    print("testing ip range")
   # ip_range = ip.ip_network('107.112.86.100/24',strict=False)
    return  ip_range
def get_ip4_Start_Address(address,cidr):
    IP_range=address+ r'/'+ cidr
    ip_Start=ip.ip_network(IP_range, strict=False)
    start_ip=ip_Start.hosts()
    start_ip=list(start_ip)
    ip_Start=dhcp_ip[0]
    return  ip_Start


def get_ip4_usable_ip(address,cidr):
    IP_range=address+ r'/'+ cidr
    usable = ip.ip_network(IP_range, strict=False)
    usable_ips = usable.hosts()
    return  usable_ips
def get_ip4_dhcp_start(address,cidr):
    print("testing method")
    IP_range=address+ r'/'+ cidr
    print("starting loop1")
    ip_dhcp=ip.ip_network(IP_range, strict=False)
    dhcp_ip=ip_dhcp.hosts()
    print("starting loop")
#     for i in ip_dhcp:
#         print(i)
#     dhcp_start=dhcp_ip
    dhcp_ip=list(dhcp_ip)
    dhcp_start=dhcp_ip[2]
    return dhcp_start
def get_ip4_dhcp_end(address,cidr):
    IP_range=address+ r'/'+ cidr
    ip_dhcp=ip.ip_network(IP_range, strict=False)
    dhcp_ip=ip_dhcp.hosts()
    dhcp_ip=list(dhcp_ip)
    dhcp_end=dhcp_ip[-1]
    return  dhcp_end

def get_ip4_gateway_address(address,cidr):
    IP_range=address+ r'/'+ cidr
    ip_gateway=ip.ip_network(IP_range, strict=False)
    gateway_ip=ip_gateway.hosts()
    gateway_ip=list(gateway_ip)
    gateway_address=gateway_ip[1]
    return  gateway_address
    
def check_ip_version(address): 
    ip_version=ip.ip_address(address).version
    return ip_version 
def get_ip4_numbered_usable_ip(address,cidr,index):
    index=int(index)
    IP_range=address+ r'/'+ cidr
    ip_numbered=ip.ip_network(IP_range, strict=False)
    numbered_ip=ip_numbered.hosts()
    numbered_ip=list(numbered_ip)
    required_index_ip=numbered_ip[index]
    return required_index_ip
def get_ipv6_address():
    ipv6_ip=ip.ip_network('2001:db8::0/103',strict=False)
    ipv6_usable=ipv6_ip.hosts()
    ipv6_usable=list(ipv6_usable)
    return ipv6_ip[-1] 

#2606:ae00:e300:008a:0000:0000:0000:0001
def calculate_ipv6_address_End(address,cidr):
       remainder = cidr%4
       multiple = cidr/4
       NumBits = multiple/4
       multipleMin =  floor(multiple)
       address = ip.ip_address(address)
       expandedIp = address.exploded
       print("remainder is  %d"  % remainder)
       print("multipleMin  is  %d"% multipleMin)
       print("exploded ip is %s"% expandedIp)
       SplitIp=expandedIp.split(":")
       print(type(SplitIp))
       newIp = SplitIp[0]+SplitIp[1]+SplitIp[2]+SplitIp[3]+SplitIp[4]+SplitIp[5]+SplitIp[6]+SplitIp[7]
       newIp=list(newIp)
       #precedingBit=int(multipleMin-1)
       if  remainder==0:
           for i in range(multipleMin,len(newIp)):
               newIp[i]='f'
       elif remainder==3:
               for i in range(multipleMin,len(newIp)):
                   newIp[i]='f'
                   newIp[multipleMin]='1'
       elif remainder==2:
               for i in range(multipleMin,len(newIp)):
                   newIp[i]='f'
                   newIp[multipleMin]='3'
                   
       elif  remainder==1:
               for i in range(multipleMin,len(newIp)):
                   newIp[i]='f'
                   newIp[multipleMin]='7'
       StringIp="".join( str(e) for e in newIp)
       print(StringIp)
       newIpEndWithColon= ':'.join(StringIp[i:i+4] for  i  in  range(0, len(StringIp), 4))
       print(newIpEndWithColon)   
       return  newIpEndWithColon
def calculate_ipv6_address_Start(address,cidr):
       remainder = cidr%4
       multiple = cidr/4
       NumBits = multiple/4
       multipleMin =  floor(multiple)
       address = ip.ip_address(address)
       expandedIp = address.exploded
       print("remainder is  %d"  % remainder)
       print("multipleMin  is  %d"% multipleMin)
       print("exploded ip is %s"% expandedIp)
       SplitIp=expandedIp.split(":")
       print(type(SplitIp))
       newIp = SplitIp[0]+SplitIp[1]+SplitIp[2]+SplitIp[3]+SplitIp[4]+SplitIp[5]+SplitIp[6]+SplitIp[7]
       newIp=list(newIp)
       #precedingBit=int(multipleMin-1)
       if  remainder==0:
           for i in range(multipleMin,len(newIp)):
               newIp[i]='0'
       elif remainder==3:
               for i in range(multipleMin,len(newIp)):
                   newIp[i]='0'
                   newIp[multipleMin]='0'
       elif remainder==2:
               for i in range(multipleMin,len(newIp)):
                   newIp[i]='0'
                   newIp[multipleMin]='0'
                   
       elif  remainder==1:
               for i in range(multipleMin,len(newIp)):
                   newIp[i]='0'
                   newIp[multipleMin]='0'
       StringIp="".join( str(e) for e in newIp)
       print(StringIp)
       newIpStartWithColon= ':'.join(StringIp[i:i+4] for  i  in  range(0, len(StringIp), 4))
       print(newIpStartWithColon)   
       return     newIpStartWithColon        
def Calculate_IpV6_Gateway(address,cidr):        
       remainder = cidr%4
       multiple = cidr/4
       NumBits = multiple/4
       multipleMin =  floor(multiple)
       address = ip.ip_address(address)
       expandedIp = address.exploded
       SplitIp=expandedIp.split(":")           
       #StringIp="".join( str(e) for e in newIp)
       newIp = SplitIp[0]+SplitIp[1]+SplitIp[2]+SplitIp[3]+SplitIp[4]+SplitIp[5]+SplitIp[6]+SplitIp[7]
       #newIp=list(newIp)
       StringIp=newIp
       #StringIp is the Ip without colons
      # print(StringIp)
       totalDigits=multiple+remainder
       length=len(StringIp)
       #getting the digits from end to the value of multiple
       splitValueHexSubnet=StringIp[int(multiple):length+1] 
       #getting the digits from beginning to value of remainder
       splitValueHexBeginning=StringIp[0:(length-int(multiple))+1] 
       #print(splitValueHexBeginning)
      # print(splitValueHexSubnet)
       #converting the last digits to int and then converting back to hex in proper format
       intValue=int(splitValueHexSubnet,16)
       Hexvalue=hex(intValue).split("x")[-1]
      # print(Hexvalue)
       #padding the hex value with required number of zeroes     
       PadHexvalue=str(Hexvalue).zfill(int(multiple)-1)
       #print(PadHexvalue)
       #increasing the integer converted last digits and then padding them with required number of zeroes
       HexIncremented=hex(intValue+1).split("x")[-1]
       #print(HexIncremented)
       PadHexIncremented=str(HexIncremented).zfill(int(multiple)-1)
       #concatenating the beginning digits and incremented hex part
       incrementedIpRaw=splitValueHexBeginning+PadHexIncremented
      # print(incrementedIpRaw)
       #print(len(incrementedIpRaw))
       incrementedIpFinal= ':'.join(incrementedIpRaw[i:i+4] for  i  in  range(0, len(incrementedIpRaw), 4))
       return incrementedIpFinal
def Calculate_IpV6_dhcp_Start(address,cidr):
       address=Calculate_IpV6_Gateway(address,cidr)        
       remainder = cidr%4
       multiple = cidr/4
       NumBits = multiple/4
       multipleMin =  floor(multiple)
       address = ip.ip_address(address)
       expandedIp = address.exploded
       SplitIp=expandedIp.split(":")           
       #StringIp="".join( str(e) for e in newIp)
       newIp = SplitIp[0]+SplitIp[1]+SplitIp[2]+SplitIp[3]+SplitIp[4]+SplitIp[5]+SplitIp[6]+SplitIp[7]
       #newIp=list(newIp)
       StringIp=newIp
       #StringIp is the Ip without colons
       #print(StringIp)
       totalDigits=multiple+remainder
       length=len(StringIp)
       #getting the digits from end to the value of multiple
       splitValueHexSubnet=StringIp[int(multiple):length+1] 
       #getting the digits from beginning to value of remainder
       splitValueHexBeginning=StringIp[0:(length-int(multiple))+1] 
       #print(splitValueHexBeginning)
       #print(splitValueHexSubnet)
       #converting the last digits to int and then converting back to hex in proper format
       intValue=int(splitValueHexSubnet,16)
       Hexvalue=hex(intValue).split("x")[-1]
       print(Hexvalue)
       #padding the hex value with required number of zeroes     
       PadHexvalue=str(Hexvalue).zfill(int(multiple)-1)
       #print(PadHexvalue)
       #increasing the integer converted last digits and then padding them with required number of zeroes
       HexIncremented=hex(intValue+1).split("x")[-1]
      # print(HexIncremented)
       PadHexIncremented=str(HexIncremented).zfill(int(multiple)-1)
       #concatenating the beginning digits and incremented hex part
       incrementedIpRaw=splitValueHexBeginning+PadHexIncremented
      # print(incrementedIpRaw)
      # print(len(incrementedIpRaw))
       incrementedIpFinal= ':'.join(incrementedIpRaw[i:i+4] for  i  in  range(0, len(incrementedIpRaw), 4))
       return incrementedIpFinal   
   


       
def get_request_call(endpoint,resource,JSONdata):
    print("trying to fetch response code for desired ip")
    print("endpoint is %s " % endpoint)
    print("resource is %s " % resource)
    headers1 = {"X-FromAppId": "Robot_Auto", "X-TransactionId": "AAI_ROBOT", "Accept": "application/json", "Content-Type": "application/json"}  
    requestKeywords= RequestsLibrary.RequestsKeywords() 
    session=requestKeywords.create_session(alias="AAI_DATA_MIG", url=endpoint, headers=headers1,verify='C:\\robot_framework\\robotsolution\\robot\\assets\\aai\\Certificates\\PEM.pem')
    print(session)
    resp=requestKeywords.put_request(alias="AAI_DATA_MIG", uri=resource,headers=headers1,json=JSONdata)#(alias, uri, data, json, params, files, headers, allow_redirects, timeout)
    #resp=requestKeywords.get_request(alias="AAI_DATA_MIG", uri=resource,headers=headers1)
     #${AAI_RESOURCE_ENDPOINT_PATH}?depth=all
    if resp.status_code!=200:
        print("ip is unused")
        print(resp.status_code) 
        print(resp.text)
        print(resp.json)
    else: 
        print("ip is used")
        print(resp.status_code) 
        print(resp.text)
        print(resp.json)
    return resp.status_code         
         
def check_for_loop(endValue):
         
          for i  in range(8, endValue,-1) :
            i-=1
            print(i)
def check_Hex_To_Int(HexValue):
    intValue=int(HexValue,16)
    print(intValue) 
    HexIncremented=hex(intValue+1).split("x")[-1]
    
    print(HexIncremented)     
    #address = ip.ip_address(address)
def check_index(StringIp):    

         length=len(StringIp)
         print(length)
         splitValueHex=StringIp[13:length]    
         print(splitValueHex)
#https://aai-uispt01-conexus.ecomp.cci.att.com:8443    /aai/v17/nodes/l3-interface-ipv6-address-list/{l3-interface-ipv6-address-list}?depth=all
def Calculate_IpV6_Gateway_unused(endpoint,resource,address,cidr):

    address = ip.ip_address(address)
    expandedIp = address.exploded
    json_data = "{"+"  "+"\"dsl\":\" cloud-region('cloud-owner','att-nc')('cloud-region-id','rdm57a') > tenant > vserver > l-interface > l3-interface-ipv4-address-list*('l3-interface-ipv4-address',"+"'"+str(address)+"') \" }"
    print(json_data)
    get_request_call(endpoint,resource,json_data)
    print()      
    return   expandedIp        

Calculate_IpV6_Gateway_unused("https://aai-uispt01-conexus.ecomp.cci.att.com:8443","aai/v16/dsl?format=resource_and_url",'169.254.194.15','79')
#Calculate_IpV6_Gateway_unused("https://aai-conexus-e2e-01.ecomp.cci.att.com:8443","aai/util/echo?action=long",'169.254.194.15','79')#/aai/util/echo?action=long
#Calculate_IpV6_Gateway_unused("https://aai-conexus-e2e-01.ecomp.cci.att.com:8443","aai/v15/network/generic-vnfs?vnf-name=zlpckgm002smt",'169.254.194.15','79')








               
#check_for_loop(0)
#check_Hex_To_Int("Efff")
#check_index("2606ae00e300008a0000000000000001")
#check_Hex_To_Int("ffffffffffffffff")
#Calculate_IpV6_Gateway("2606:ae00:e300:008a:0000:0000:0000:0001",79)  

#get_request_call("https://aai-conexus-e2e-02.ecomp.cci.att.com:8443","aai/v17/nodes/l3-interface-ipv6-address-list/2001%3A1892%3A2002%3A0%3A0%3A0%3A0%3A5?depth=all")






     
#calculate_ipv6_address_Range("::",2)
# calculate_ipv6_address_Range("2002:db8::",77)
# calculate_ipv6_address_Start("2002:db8::",77)

#calculate_ipv6_address_Range("2606:ae00:e300:008a:0000:0000:0000:0001",33)
#calculate_ipv6_address_Range("2001:db8:85a3::8a2e:370:7334",127)


    
      






