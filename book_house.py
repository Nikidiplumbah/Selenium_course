from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5[id='price']"),'$100'))

button = browser.find_element(By.CSS_SELECTOR, "button[id='book']")
button.click()

time.sleep(1)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

element_x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
value_x = element_x.text 
x = value_x
y = calc(x)

input = browser.find_element(By.CSS_SELECTOR, "#answer")
input.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
browser.execute_script('arguments[0].disabled = false;', button)
button.click()

time.sleep(5)
browser.quit()