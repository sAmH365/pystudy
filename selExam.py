from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


# 사이트 접속하기
driver.get('https://instagram.com')
time.sleep(2)
e = driver.find_element(By.CLASS_NAME, '_aa4u').text
print(e)


