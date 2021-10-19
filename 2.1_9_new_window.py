from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(".trollface.btn.btn-primary").click()

    #переключение на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    

    element_x = browser.find_element_by_css_selector('#input_value')
    x = int(element_x.text)

    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(calc(x))


    browser.find_element_by_css_selector('.btn.btn-primary').click()


    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
