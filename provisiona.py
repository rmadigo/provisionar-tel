"""Import necessarios nesse modulo"""
from playwright.sync_api import sync_playwright
from time import sleep
import logging
import sys

def provisionar(ip: str, mac: str):
    """Navega na pagina do telefone configura"""

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('logs.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
    
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

        # Auto Provision
        page.locator('//*[@id="Settings"]/div').click()
        page.locator('//*[@id="SettingAutop"]').click()
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[6]/div/div[1]/input').click()
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[6]/div/div[1]/input').fill(server_url)
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[7]/div/div[1]/input').click()
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[7]/div/div[1]/input').fill(user)
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[8]/div/div[1]/input').click()
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[8]/div/div[1]/input').fill(pwd)

        page.locator('//*[@id="y-submit-confirm"]/button').click()
        page.locator('//*[@id="Status"]/div').click()
        page.locator('//*[@id="Status"]/div').click()
        # sleep(10)
        # print(page.title())
        browser.close()
        logger.info('O telefone %s foi provisionado', mac)


if __name__ == "__main__":
    provisionar("10.17.27.136", "24:9a:d8:61:61:09")
