from playwright.sync_api import sync_playwright
from time import sleep 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(
        ignore_https_errors=True,
        http_credentials={"username": "admin", "password": "admin"}
    )
    page.goto("https://10.17.11.28")
    page.locator('//*[@id="idUsername"]').click()

    page.locator('//*[@id="idUsername"]').fill("admin")
    page.locator('//*[@id="idPassword"]').click()
    page.locator('//*[@id="idPassword"]').fill("admin")
    page.locator('//*[@id="idLogin"]').click()
    page.locator('//*[@id="Security"]/div').click()
    page.locator('//*[@id="SecurityTrustedCert"]').click()
    page.locator('//*[@id="security-trustedcert"]/form/div[1]/div[2]/div[2]/div/div/span').click()
    print(page.title())
    # sleep(100)
    # browser.close()
