from scapy.all import *

packets = rdpcap('file.pcap')

for packet in packets:
    print(packets)
