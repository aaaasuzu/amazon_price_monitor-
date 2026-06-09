import time
import random
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



# ドライバー起動
def create_driver():
    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")

    if platform.system() == "Linux":
        driver = webdriver.Chrome(options=options)

    else:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    return driver

#価格取得
def get_price(driver, url):
    driver.get(url)

    # ランダム待機(bot対策)
    time.sleep(random.uniform(3,6))

    try:
        # 価格(通常)
        price = driver.find_element(By.ID,"priceblock_ourprice").text
    except:
        try:
            #パターン別
            price = driver.find_element(By.CLASS_NAME,"a-price-whole").text
        except:
            #セール価格
            price = driver.find_element(By.ID,"priceblock_dealprice").text
        #数字だけ
    price = price.replace("￥","").replace(",","")
    return int(price)
   