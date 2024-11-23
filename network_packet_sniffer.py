from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst 
        protocol = packet[IP].proto 
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")

        if TCP in packet:
            print(f"  TCP Packet - Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"  UDP Packet - Source Port: {packet[UDP].sport}, Destination Port: {packet[UDP].dport}")

sniff(prn=packet_callback,iface="eth0",filter="ip",store=0)
   