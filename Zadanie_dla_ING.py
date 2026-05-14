from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:


    time.sleep(0.1)
    browser = p.chromium.launch() 
    page = browser.new_page()
    page.goto("https://ing.pl")   
    #Otwarcie ustawień cookies
    page.click("button.js-cookie-policy-deputed-settings-button")
    time.sleep(1)
    #Odznaczenie cookies analitycznych
    page.locator('div[role="switch"][name="CpmAnalyticalOption"]').click(force=True)
    time.sleep(1)
    #Potwierdzenia ustawień
    page.click("text=Zaakceptuj zaznaczone",force=True)
    #Weryfikacja pobranych cookies: 
    print("Zapisane pliki cookies:")
    cookies = page.context.cookies()
    for cookie in cookies:
        print(cookie["name"], cookie["value"])
    # Zapewnienie powtarzalności skryptu:
    page.context.clear_cookies()
    browser.close()
    input('Egzekucja udana. Potwierdź ZAMKNIĘCIE skryptu.')