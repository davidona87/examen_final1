from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver

driver = webdriver.Chrome()
driver.get("https://www.muchomejorec.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#buscar_todo")
search_box.send_keys("laptop")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#search-submit > i")
search_button.click()

articles = driver.find_elements(By.CSS_SELECTOR, "body > section > section > div > div > div > section > div ")

mongodb = MongoDriver()

for lapt in articles:
    try:
        title = lapt.find_element(By.CSS_SELECTOR, "body > section > section > div > div > div > section > div > div:nth-child(2) > div > div > div > a:nth-child(1) > div.marca > span").text
        description = lapt.find_element(By.CSS_SELECTOR, "body > section > section > div > div > div > section > div > div:nth-child(2) > div > div > div > a:nth-child(1) > div.aparecer > p").text
        price = lapt.find_element(By.CSS_SELECTOR, "body > section > section > div > div > div > section > div > div:nth-child(2) > div > div > div > a:nth-child(1) > h5.precio").text
        print(title)
        print(description)
        print(f"{price}")

        artic = {
            "Título": title,
            "Descripción": description,
            "Precio": price
        }



        mongodb.insert_record(record=artic, username="suministros")

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()