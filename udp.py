from scapy.all import *

def udp_spoof(ip_src, ip_dst, src_port, dst_port, payload):
    ip_header = IP(src=ip_src, dst=ip_dst)
    
    udp_header = UDP(sport=src_port, dport=dst_port)
    
    packet = ip_header / udp_header / Raw(payload)
    
    print(f"Sending spoofed UDP packet from {ip_src}:{src_port} to {ip_dst}:{dst_port}")
    print(f"Payload: {payload}")
    
    send(packet, count=1)
    
    print(f"Spoofed UDP packet successfully sent!")

ip_src = "192.168.1.100"  # Spoofed source IP address
ip_dst = "192.168.1.200"  
src_port = 12345           
dst_port = 53              
payload = b"001020102010201021" 

udp_spoof(ip_src, ip_dst, src_port, dst_port, payload)
