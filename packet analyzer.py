from scapy.all import *

# Function to analyze packets
def packet_callback(packet):
    # Extract relevant information from the packet
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        # Display packet information
        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {protocol}")
        
        # Display additional information based on the protocol
        if TCP in packet:
            print(f"TCP Packet | Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"UDP Packet | Source Port: {packet[UDP].sport}, Destination Port: {packet[UDP].dport}")
        
        # Print payload data (if any)
        if Raw in packet:
            print(f"Payload: {packet[Raw].load}")
        print("-" * 50)

# Start sniffing on the interface (e.g., eth0 for Linux, or en0 for macOS)
print("Starting packet capture...")
sniff(filter="ip", prn=packet_callback, store=0)
