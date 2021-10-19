from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("[name='firstname']")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector("[name='lastname']")
    last_name.send_keys("Ivan")
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("mail@mail.com")

    with open("file.txt", "w") as file:
        content = file.write("Hello World")  # create test.txt file
    
    # получаем путь к директории текущего исполняемого скрипта
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    # имя файла, который будем загружать на сайт. файо дб в той же папке что и скрипт
    file_name = "file.txt"
    
    file_path = os.path.join(current_dir, file_name)

    upload = browser.find_element_by_css_selector("#file")
    upload.send_keys(file_path)
    



    button = browser.find_element_by_tag_name("button")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
