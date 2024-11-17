import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

def main(data):
    output = ''

    ua = UserAgent()
    user_agent = ua.random

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-agent={user_agent}")

    extension_path = "./keplr.crx"
    chrome_options.add_extension(extension_path)

    driver = webdriver.Chrome(options=chrome_options)

    driver.delete_all_cookies()

    driver.get("https://2ip.ru/")
    time.sleep(5)

    ip_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div[1]/section[1]/div/div[1]/div/div[1]/span')
    ip = ip_element.text.strip()

    if ip == "93.95.229.145":
        print("IP-адрес не изменен, возможно, прокси не работает корректно.")
    time.sleep(3)

    windows = driver.window_handles
    extension_url = "chrome-extension://dmkamcknogkgcdfhhbddcghachkejeap/register.html#"

    for window in windows:
        driver.switch_to.window(window)
        if extension_url in driver.current_url:
            break

    # Продолжение автоматизации с использованием данных из JSON
    button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div/div/div[3]/div[3]/button')
    button.click()
    time.sleep(1)

    button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[5]/button')
    button.click()
    time.sleep(1)

    button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[3]/div/div/form/div[1]/div/button[3]')
    button.click()
    time.sleep(1)

    input_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[3]/div/div/form/div[3]/div/div/div[1]/div/div[2]/div/div/input')
    input_field.click()
    input_field.send_keys(data['priv_key'])

    button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[3]/div/div/form/div[5]/div/button')
    button.click()
    time.sleep(1)

    input_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[4]/div/div/form/div/div[1]/div[2]/div/div/input')
    input_field.click()
    input_field.send_keys(data['priv_key'])

    input_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[4]/div/div/form/div/div[3]/div[2]/div/div/input')
    input_field.click()
    input_field.send_keys(data['priv_key'])

    input_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[4]/div/div/form/div/div[5]/div[2]/div/div/input')
    input_field.click()
    input_field.send_keys(data['priv_key'])

    button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[4]/div/div/form/div/div[7]/button')
    button.click()
    time.sleep(7)

    button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div/div/div/div[10]/div/button')
    button.click()

    driver.get("https://verifier.nillion.com/")
    time.sleep(4)

    button = driver.find_element(By.XPATH, '//*[@id="navigation-top"]/div/div[1]/button')
    button.click()

    time.sleep(6)
    try:
        driver.switch_to.window(driver.window_handles[-1])
        approve_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[3]/div/button')
        approve_button.click()
        time.sleep(2)
    except Exception as e:
        output = json.dumps({"status": "failed", "message": "keplr failed connect"})

    driver.switch_to.window(driver.window_handles[1])

    button = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/section/div[1]/button[2]')
    button.click()
    time.sleep(1)

    button = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/section/div/div[2]/button[2]')
    button.click()
    time.sleep(1)

    button = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/div[3]/div[2]/div[2]/div/div[5]/div[1]/button[1]')
    button.click()
    time.sleep(3)

    button = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/div[3]/div[2]/div[2]')
    button.click()
    time.sleep(1)

    input_field = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/div[3]/div[2]/div[2]/div/div[5]/div[2]/div/form/label[1]')
    input_field.click()
    time.sleep(1)
    input_field.send_keys(data['address'])

    input_field = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/div[3]/div[2]/div[2]/div/div[5]/div[2]/div/form/label[2]')
    input_field.click()
    time.sleep(1)
    input_field.send_keys(data['pub_key'])

    button = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/div[3]/div[2]/div[2]/div/div[5]/div[2]/div/form/button')
    button.click()
    time.sleep(7)

    time.sleep(6)
    try:
        driver.switch_to.window(driver.window_handles[-1])

        button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[3]/button')
        button.click()

        time.sleep(11)
    except Exception as e:
        output = json.dumps({"status": "failed", "message": "keplr failed connect"})

    driver.switch_to.window(driver.window_handles[1])

    result = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/div[3]/div[2]/div[2]/div/div[5]/div[2]/div/form/button')

    if "VERIFIER REGISTERED" in result.text:
        output = json.dumps({"status": "success"})
    else:
        result = driver.find_element(By.XPATH, '/html/body/main/astro-island/main/div[3]/div[2]/div[2]/div/div[5]/div[2]/div/form/span')
        output = json.dumps({"status": result.text})

    print(output)
    driver.quit()

# Пример использования с JSON-вводом
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read()  # Чтение JSON-данных с входа
    data = json.loads(input_data)  # Преобразуем строку JSON в Python-объект
    main(data)
