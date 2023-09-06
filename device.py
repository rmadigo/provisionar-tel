"""
Import na utilizados na classe Device
device.py
"""
from dataclasses import dataclass
from time import sleep
import requests
from tqdm import tqdm
from scapy.all import ARP, Ether, srp, Dot1Q, ls, sendp
from provisiona import provisionar_yealink


@dataclass
class Device():
    """Classe representando Device"""
    ip: str
    mac: str
    vendor: str


def mac_vendor(mac):
    """Função para consultar o fabricante com base no endereço MAC"""
    try:
        response = requests.get('http://api.macvendors.com/' + mac, timeout=10)
        if response.status_code == 200:
            return response.text
    except Exception as error:
        print(f"Erro ao consultar fabricante: {str(error)}")
    return "Desconhecido"


def scan(localizados):
    """Funcao scanner rede sem paremetros"""
    request = ARP()
    request.pdst = '10.17.11.1/24'
    # request.psrc = '10.17.12.2'
    # print(request.summary())
    broadcast = Ether()
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    request_broadcast = broadcast / request
    # print(ls(request_broadcast))
    clientes = srp(
        request_broadcast,
        timeout=1,
        # verbose=True
        )[0]

    print(clientes)
    # for i in tqdm(range(10)):
    for cliente in clientes:
        mac_cliente = cliente[1].hwsrc
        ip_cliente = cliente[1].psrc
        print(f"Dispositivo encontrado - IP: {ip_cliente}, MAC: {mac_cliente}")

        if mac_cliente in localizados:
            print("MAC já verificado!!!")
        else:
            print("MAC Novo localizado!!!")
            vendor = mac_vendor(mac_cliente)
            print(f"Fabricante: {vendor}")
            if "yealink" in vendor.lower():
                provisionar_yealink(ip_cliente, mac_cliente)
            elif "grandstream" in vendor.lower():
                pass
            localizados.append(mac_cliente)

    return localizados


if __name__ == "__main__":
    scan([])
    # mac_vendor("24:9A:D8:61:61:09")
