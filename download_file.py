from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = ('http://suninjuly.github.io/file_input.html')
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By. CSS_SELECTOR, "input[placeholder='Enter first name']")
input1.send_keys('Nikita')
input1 = browser.find_element(By. CSS_SELECTOR, "input[placeholder='Enter last name']")
input1.send_keys('Kond')
input1 = browser.find_element(By. CSS_SELECTOR, "input[placeholder='Enter email']")
input1.send_keys('tester88@mail.su')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

upload = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
upload.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

time.sleep(10)
browser.quit()

