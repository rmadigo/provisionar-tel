"""Import necessarios nesse modulo"""
import json
from playwright.sync_api import sync_playwright
from time import sleep
from logging_configure import logger


def provisiona_ramal(ramal: str, mac: str):
    """Navega na pagina do telefone configura"""
    try:
        # print("http://"+ip)
        server_url = "xsp.gc.italk.net.br:443/dms/YealinkT4xTemplate/" + \
            mac.replace(":", "")+".cfg"
        user = "voicemanagerDMS"
        pwd = "q3B~2#MrUsZT!V01c3"

        device = ""

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page(
                ignore_https_errors=True,
            )
            page.goto("https://xsp.gc.italk.net.br/")
            # Login
            page.locator('[name="EnteredUserID"]').fill("provisionar_boot@mpt.mp.br")
            page.locator('[name="Password"]').fill("Acesso@mpt#2023")
            page.locator('//html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td/a').click()

            sleep(1)
            # Usuarios
            page.locator('[name="/Group/Members/"]').click()
            # Ramal
            page.locator('[name="findKey0"]').select_option('Ramal')
            page.locator('//*[@id="findValue0"]').fill(ramal)
            sleep(1)
            page.locator('//*[@id="search0"]').click()

            # Editar
            page.locator('//*[@id="Row1"]/td[16]/a').click()
            page.locator('[name="/User/Addresses/"]').click()

            page.locator('[name="deviceName"]').select_option('New Device')
            
            # Tipo de perfil aparelho:
            if "249ad861" in mac.lower():
                device = "YEAT43U_272125" + ramal
                page.locator('[name="newDeviceType"]').select_option('YealinkT4xTemplate')
                
                page.locator('[name="newDeviceName"]').fill(device)
                page.locator('[name="macAddress"]').fill(mac.replace(":", "").upper())
            elif "c074adca" in mac.lower(): 
                device = "GXP2170_272125" + ramal
                page.locator('[name="newDeviceType"]').select_option('Grandstream GXP21XX')
                page.locator('[name="newDeviceName"]').fill(device)
                page.locator('[name="macAddress"]').fill(mac.replace(":", "").upper())
            
            page.locator('[name="deviceLinePortDomain"]').fill("272125" + ramal)

            # OK

            page.locator('//*[@id="buttonbarbottom"]/td/input[2]').click()

            # //*[@id="findKey0"]/option[5]


            sleep(1)
            # print(page.title())
            # browser.close()
            # Registre o sucesso do provisionamento
            logger.info('O ramal %s foi provisionado', ramal)

    except Exception as e:
        logger.error(f"Erro durante o provisionamento: {str(e)}")


if __name__ == "__main__":
    # provisionar_yealink("10.17.11.23", "24:9A:D8:61:5B:58")
    # provisiona_ramal("4523", "C0:74:AD:CA:DB:76")
    with open("ConfiguraRamal.json", "r", encoding="utf-8") as arquivo:
        ramais = json.load(arquivo)

        for m in ramais:
            item = m.split(',')
            provisiona_ramal(item[1], item[0])
            # print(f'{m.split(',')}')
