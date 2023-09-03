"""
Import na utilizados na classe Device
device.py
"""
from dataclasses import dataclass
from typing import List, Dict
from scapy.all import ARP, Ether, srp, ls
import requests
from time import sleep
from provisiona import provisionar

@dataclass
class Device():
    """Classe representando Device"""
    ip: str
    mac: str
    vendor: str

def mac_vendor(mac):
    """Funcao retorna fabricante do MAC"""
    sleep(3)
    vendor = requests.get(
        'http://api.macvendors.com/'+mac, timeout=10).text
    if "yealink" in vendor.lower():
        print("FAZER Provicionamento")
        print(f"MAC fabricante: {vendor}")
        return True
    else:
        print(f"MAC fabricante: {vendor}")
        return False


def scan(localizados):
    """Funcao scanner rede sem paremetros"""

    request = ARP()
    request.pdst = '10.17.11.1/24'
    # request.psrc = '10.17.11.2'
    # print(request.summary())
    broadcast = Ether()
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    request_broadcast = broadcast / request

    # print(ls(request_broadcast))
    clientes = srp(
        request_broadcast,
        timeout=1,
        verbose=False
        )[0]

    for cliente in clientes:        
        # cliente_dict = {
        #     "mac": cliente[1].hwsrc,
        #     "ip": cliente[1].psrc,
        #     "vendor": requests.get(
        #         'http://api.macvendors.com/'+cliente[1].hwsrc, timeout=10).text
        # }
        mac = cliente[1].hwsrc
        ip = cliente[1].psrc

        if mac in localizados:
            print("MAC ja verificado!!!")
            continue
        else:
            print("MAC novo localizado!!!")
            if(mac_vendor(mac)):
                provisionar(ip, mac)
        localizados.append(mac)

    return localizados


if __name__ == "__main__":
    mac_vendor("24:9A:D8:61:61:09")
