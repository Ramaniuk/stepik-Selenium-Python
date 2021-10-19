from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

# time.sleep(1)
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
