from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    #browser.execute_script("alert('Robots at work');")
    #browser.execute_script('document.title="Script executing";')
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
