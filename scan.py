from scapy.all import ARP, Ether, srp


def scan(ip):
    arp_req_frame = ARP(pdst=ip)

    broadcast_ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = srp(
        broadcast_ether_arp_req_frame, timeout=1, verbose=False)[0]
    result = []
    for i in range(0,len(answered_list)):
        client_dict = {
            "ip": answered_list[i][1].psrc, 
            "mac": answered_list[i][1].hwsrc}
        result.append(client_dict)
    return result
