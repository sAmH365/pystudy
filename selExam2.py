from selenium import webdriver
import pyautogui
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyperclip
from selenium.webdriver.common.keys import Keys
import platform
from selenium.webdriver.common.action_chains import ActionChains
import time

# 크롬 드라이버 옵션 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# 새로운 창 생성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://naver.com')

# 현재 열려 있는 창 가져오기
current_window_handle = driver.current_window_handle

# <a href class='MyView-module__link_login___HpHMW'> 일때 해당 링크 클릭
driver.find_element(By.XPATH, "//a[@class='MyView-module__link_login___HpHMW']").click()

# 새롭게 생성된 탭의 핸들을 찾습니다
# 만일 새로운 탭이 없을경우 기존 탭을 사용합니다.
new_window_handle = None
for handle in driver.window_handles:
    if handle != current_window_handle:
        new_window_handle = handle
        break
    else:
        new_window_handle = handle


# 새로운 탭을 driver2로 지정합니다
driver.switch_to.window(new_window_handle)
driver2 = driver

username = driver2.find_element(By.NAME, 'id')
pw = driver2.find_element(By.NAME, 'pw')

input_id="npower5377"
input_pw="3250med2@"

ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

#ID input 클릭
username.click()
#js를 사용해서 붙여넣기 발동 <- 왜 일부러 이러냐면 pypyautogui랑 pyperclip를 사용해서 복붙 기능을 했는데 운영체제때문에 안되서 이렇게 한거다.
driver2.execute_script("arguments[0].value = arguments[1]", username, input_id)
time.sleep(1)

pw.click()
driver2.execute_script("arguments[0].value = arguments[1]", pw, input_pw)
time.sleep(1)

#입력을 완료하면 로그인 버튼 클릭
driver2.find_element(By.CLASS_NAME, "btn_login").click()
