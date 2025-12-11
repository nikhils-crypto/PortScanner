import subprocess
from optparse import OptionParser
import re

def get_arguments():
    parser = OptionParser()
    parser.add_option("-i" , "--interface" , dest="Interface" , help="Enter the Interface to change the mac address")
    parser.add_option("-m" , "--mac" , dest="new_mac" , help="Enter the new mac address in order to change the previous one")
    (options,args) = parser.parse_args()
    if not options.Interface:
        parser.error("Please specify the Interface to change the mac address")
    elif not options.new_mac:
        parser.error("Please specify the new mac address")
    return options

def change_mac(Interface , new_mac):
    print("[+] Changing the mac address for: " + Interface + "to" + new_mac)
    subprocess.call(["ifconfig" , Interface , "down"])
    subprocess.call(["ifconfig" , Interface , "hw" , "ether" , new_mac])
    subprocess.call(["ifconfig" , Interface , "up"])

def get_mac(Interface):
    find_mac = subprocess.check_output(["ifconfig" , Interface])
    search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", find_mac)
    if not search_mac:
        print("[!] Could find the mac address")
    else:
        return search_mac.group(0)
options = get_arguments()
change_mac(options.Interface , options.new_mac)
current_mac = get_mac(options.Interface)
if current_mac == options.new_mac:
    print("[+] MAC address changed")
else:
    print("[-] MAC address is not changed")
