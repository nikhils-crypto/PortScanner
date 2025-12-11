from optparse import OptionParser
from socket import *
from threading import *

nik = Semaphore(value=1)
def target_Scan(target_Host , target_Port):
    try:
        target_Scan = socket(AF_INET , SOCK_STREAM)
        target_Scan.connect((target_Host , target_Port))
        target_Scan.send("Hi , How re you?\r\n")
        result = target_Scan.recv(100)
        nik.acquire()
        print("[+] %d/tcp opened"%target_Port)
        print("[+] Banner Flag: " + str(result))
    except:
        nik.acquire()
        print("[-] %d/tcp closed"%target_Port)
    finally:
        nik.release()
        target_Scan.close()

def portScan(target_Host , target_Ports):
    try:
        target_IP = gethostbyname(target_Host)
    except:
        print("[-] cannot resolve '%s': unknown Host"%target_Host)
        return
    try:
        target_Name = gethostbyaddr(target_IP)
        print("[+] scanning results for: " + target_Name)
    except:
        print("[+] scanning results for: " + target_IP)
    setdefaulttimeout(1)
    for target_Port in target_Ports:
        t = Thread(target=target_Scan , args =(target_Host , int(target_Port)))
        t.start()
def get_arguments():
    parser = OptionParser()
    parser.add_option("-H" , dest="target_Host" , type="string" , help="Enter the target host")
    parser.add_option("-p" , dest="target_Port" , type="string" , help="Enter the target port")
    (options, args) = parser.parse_args()
    if not options.target_Host:
        parser.error("[-] PLease specify the host")
    elif not options.target_Port:
        parser.error("[-] Please specify the target port")

    return options
options = get_arguments()
target_Host = options.target_Host
target_Ports = str(options.target_Port).split(',')
portScan(target_Host , target_Ports)