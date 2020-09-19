from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    URL = 'https://investmoscow.upt24.ru/'
    TITLE = 'Главная - Инвестиционный портал Москвы'
    LOGIN_PIC = (By.ID, 'auth-bt')
    LOGIN_INPUT = (By.ID, 'Login')
    PASSWORD_INPUT = (By.ID, 'Password')
    AUTH_BUTTON = (By.ID, 'authbtn')
    LINK_TO_ONLINE_SERVICES_PAGE = (By.XPATH, '//*[@id="first-navbar"]/ul/li[4]/a')
    LOGIN = 'ilyaaanichkin@yandex.ru'
    PASSWORD = '1234567'
    HEADER_USER_NAME = (By.XPATH, '//*[@id="auth-bt"]/a/span')

    def __init__(self, driver):

        self.driver = driver

    def get_title(self):
        
        return self.driver.title
    

    def get_header_user_name(self):

        header = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPage.HEADER_USER_NAME))
        return header

    def go_to_online_services_page(self):
        
        link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPage.LINK_TO_ONLINE_SERVICES_PAGE))
        link.click()

    def login(self):

        login_pic = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPage.LOGIN_PIC))
        login_pic.click()
        login_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPage.LOGIN_INPUT))
        login_input.send_keys(MainPage.LOGIN)
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPage.PASSWORD_INPUT))
        password_input.send_keys(MainPage.PASSWORD)
        auth_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPage.AUTH_BUTTON))
        auth_button.click()
        
