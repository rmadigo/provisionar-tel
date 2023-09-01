from scapy.all import ARP, Ether, srp, ls, ICMP, srp1, IP, sr1


def scan(ip):
    arp_req_frame = ARP(pdst=ip)

    # print(srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/IP()/ICMP()))
    print(10*'*')
    print(sr1(IP(dst="192.168.15.1")/ICMP()))
    broadcast_ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    # answered_list = srp(broadcast_ether_arp_req_frame,
    #                     timeout=1,
    #                     verbose=False)
    
    # print('Total Number of Responses ->', len(answered_list))
    # print('-----------Answered Responses---------')
    # print('Number of Answered Responsed ->', len(answered_list[0]))
    # print()
    # for i in range(0, len(answered_list[0])):
    #     print(answered_list[0][i])
    #     print()
    # print('-----------UnAnswered Responses---------')
    # print('Number of UnAnswered Responsed ->', len(answered_list[1]))
    # print()
    # for i in range(0, len(answered_list[1])):
    #     print(answered_list[1][i])
    #     print()


    # answered_list = srp(
    #     broadcast_ether_arp_req_frame,
    #     timeout=5,
    #     verbose=True)[0]

    result = []
    for i in range(0, len(answered_list)):
        client_dict = {
            "ip": answered_list[i][1].psrc, 
            "mac": answered_list[i][1].hwsrc}
        result.append(client_dict)
    return result
