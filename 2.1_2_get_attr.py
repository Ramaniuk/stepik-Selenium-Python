from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    treasure = browser.find_element_by_css_selector("#treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radiobtn = browser.find_element_by_css_selector("#robotsRule")
    radiobtn.click()

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
