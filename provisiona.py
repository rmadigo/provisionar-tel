"""Import necessarios nesse modulo"""
from playwright.sync_api import sync_playwright
from time import sleep


def provisionar(ip: str):
    """Navega na pagina do telefone configura"""
    print("http://"+ip)
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
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[6]/div/div[1]/input').fill("https://xsp.gc.italk.net.br:443/dms/YealinkT4xTemplate//249ad8616109.cfg")
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[7]/div/div[1]/input').click()
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[7]/div/div[1]/input').fill("voicemanagerDMS")
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[8]/div/div[1]/input').click()
        page.locator('//*[@id="setting-autop"]/form/div[1]/div[2]/div[8]/div/div[1]/input').fill("q3B~2#MrUsZT!V01c3")

        page.locator('//*[@id="y-submit-confirm"]/button').click()
        # print(page.title())
        # browser.close()


if __name__ == "__main__":
    provisionar("10.17.27.136")
