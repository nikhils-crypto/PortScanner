import scapy.all as scapy
from optparse import OptionParser

def get_arguments():
    parser = OptionParser()
    parser.add_option('-i' , '--ip' , dest='IP' , help="Enter the ip address to scan")
    (option,args) = parser.parse_args()
    if not option.IP:
        parser.error("Please specify the ip address or ip range to scan")
    else:
        return option

def scan(ip):
    arp = scapy.ARP(op=1 , pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/arp
    answered_list = scapy.srp(packet , timeout=1, verbose=False)[0]

    client_list = []
    for a in answered_list:
        client_dict = {
                        "source_ip": a[0].psrc,
                        "source_mac": a[0].hwsrc,
                        "received_ip": a[1].psrc,
                        "received_mac": a[1].hwsrc
                      }
        client_list.append(client_dict)
    return client_list

def print_me(result_list):
    print("\n...................................................................................................................................\nSource_ip\t\t\tSource_mac\t\t\t\tReceived_ip\t\t\tReceived_mac\n...................................................................................................................................\n")
    for client in result_list:
        print(client["source_ip"] + "\t\t\t" + client["source_mac"] + "\t\t\t" + client["received_ip"] + "\t\t\t" + client["received_mac"])

option = get_arguments()
client_list = scan(option.IP)
print_me(client_list)

