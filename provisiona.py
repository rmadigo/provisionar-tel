"""Import necessarios nesse modulo"""
import os
from playwright.sync_api import sync_playwright
from time import sleep
from logging_configure import logger

def provisionar_yealink(ip: str, mac: str):
    """Navega na pagina do telefone configura"""
    try:
        # print("http://"+ip)
        server_url = "https://xsp.gc.italk.net.br:443/dms/YealinkT4xTemplate/" + \
            mac.replace(":", "")+".cfg"
        user = "voicemanagerDMS"
        pwd = "q3B~2#MrUsZT!V01c3"

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page(
                ignore_https_errors=True,
                http_credentials={"username": "admin", "password": "admin"}
            )
            page.goto("http://"+ip)
            # Login
            page.locator('//*[@id="idUsername"]').click()
            page.locator('//*[@id="idUsername"]').fill("admin")
            page.locator('//*[@id="idPassword"]').click()
            page.locator('//*[@id="idPassword"]').fill("admin")
            page.locator('//*[@id="idLogin"]').click()

            # Only Accept Trusted Certificates
            page.locator('//*[@id="Security"]/div').click()
            page.locator('//*[@id="SecurityTrustedCert"]').click()
            page.locator('//*[@id="security-trustedcert"]/form/div[1]/div[2]/div[2]/div/div/span').click()
            page.locator('//*[@id="y-submit-confirm"]/button').click()
            sleep(1)
            # Auto Provision
            page.locator('//*[@id="Status"]/div').click()
            page.locator('//*[@id="Status"]/div').click()
            
            page.locator('//*[@id="Settings"]/div').click()
            sleep(1)
            page.locator('//*[@id="SettingAutop"]').click()
            sleep(1)
            page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[6]/div/div[1]/input').click()
            page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[6]/div/div[1]/input').fill(server_url)
            page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[7]/div/div[1]/input').click()
            page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[7]/div/div[1]/input').fill(user)
            page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[8]/div/div[1]/input').click()
            page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[8]/div/div[1]/input').fill(pwd)
            sleep(1)
            page.locator('//*[@id="y-submit-confirm"]/button').click()
            page.locator('//*[@id="Status"]/div').click()
            page.locator('//*[@id="Status"]/div').click()
            # sleep(10)
            # print(page.title())
            browser.close()
            # Registre o sucesso do provisionamento
            logger.info('O telefone %s foi provisionado', mac)

    except Exception as e:
        logger.error(f"Erro durante o provisionamento: {str(e)}")


def provisionar_grandstream(ip: str, mac: str):
    """Navega na pagina do telefone configura"""
    try:

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page(
                ignore_https_errors=True,
                http_credentials={"username": "admin", "password": "admin"}
            )
            page.goto("http://"+ip)
            #logar
            page.locator('//*[@id="control-pad"]/div[1]/div[2]/input').click()
            page.locator('//*[@id="control-pad"]/div[1]/div[2]/input').fill("admin")
            page.locator('//*[@id="control-pad"]/div[2]/div[2]/input').click()
            page.locator('//*[@id="control-pad"]/div[2]/div[2]/input').fill("laboral")
            page.locator('//*[@id="control-pad"]/div[2]/div[2]/button').click()
            
            #Atualizar firmware
            diretorio_atual = os.getcwd()
            arquivo_caminho = os.path.join(diretorio_atual, 'firmware_tel\\gxp2170fw.bin')

            page.locator('//*[@id="gwt-uid-188"]').click()
            page.locator('//*[@id="left-pad"]/div/div[2]/div[2]/div[1]').click()
            page.locator('//*[@id="elm-57"]/button').click()
            sleep(30)
            # page.locator('/html/body/div[5]/div/div/div/div[2]/div/div/div').click()



            

    except Exception as e:
        print(e)


if __name__ == "__main__":
    # provisionar_yealink("10.17.11.28", "24:9A:D8:61:5B:58")
    provisionar_grandstream("10.17.11.27", "24:9A:D8:61:5B:58")

