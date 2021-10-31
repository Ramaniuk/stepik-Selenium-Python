
import time

    

def test_find_the_button(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")

    assert len(button) == 1, '!!! Error !!!'

