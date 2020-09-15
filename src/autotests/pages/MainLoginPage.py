from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainLoginPage:

    URL = 'https://investmoscow.upt24.ru/'
    LOGIN_PIC = (By.ID, 'auth-btns')
    LOGIN_INPUT = (By.ID, 'Login')
    PASSWORD_INPUT = (By.ID, 'Password')
    LOGIN = 'ilyaaanichkin@yandex.ru'
    PASSWORD = '1234567'

    def __init__(self, driver):

        self.driver = driver

    def get_title(self):
        return self.driver.title

    def press_to_login_pic(self):

        login_pic = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainLoginPage.LOGIN_PIC))
        login_pic.click()
        login_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainLoginPage.LOGIN_INPUT))
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainLoginPage.PASSWORD_INPUT))
        return login_input, password_input
