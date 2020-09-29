from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://ege.edu.tr/tr-0/anasayfa.html")
print(driver.title)

search = driver.find_element_by_id("srch_fld")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.CLASS_NAME,"container"))
    #print(main.text)
    articles = main.find_elements_by("a")
    for article in articles:
        header = article.find_elements_by_class_name("entry-title")
        print(header.text)
finally:
    driver.quit()

#main = driver.find_element_by_id("search")

# print(driver.page_source)
time.sleep(5)

driver.quit()
