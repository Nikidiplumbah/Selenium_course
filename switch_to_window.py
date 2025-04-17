from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = ('http://suninjuly.github.io/redirect_accept.html')
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

submit1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit1.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

element_x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
value_x = element_x.text 
x = value_x
y = calc(x)

input = browser.find_element(By.CSS_SELECTOR, "#answer")
input.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

time.sleep(10)
browser.quit()