from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    num1_element = browser.find_element_by_css_selector("#num1")
    num1 = num1_element.text
    num2_element = browser.find_element_by_css_selector("#num2")
    num2 = num2_element.text
    number = int(num1) + int(num2)
    print(number)

    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(number))



    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
