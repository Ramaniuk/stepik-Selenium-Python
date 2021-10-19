from selenium import webdriver
import time
import math

def calc(num):
    return math.log(abs(12*math.sin(num)))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    fun = calc(int(x))
    print(fun)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(str(fun))
    chekbox = browser.find_element_by_css_selector("#robotCheckbox")
    chekbox.click()

    radiobtn = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()
    

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
