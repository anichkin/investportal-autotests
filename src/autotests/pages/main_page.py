from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import allure


class MainPage(BasePage):

    PATH = ''
    TITLE = 'Главная - Инвестиционный портал Москвы'
    LOGIN_PIC = (By.ID, 'auth-bt')
    LOGIN_INPUT = (By.ID, 'Login')
    PASSWORD_INPUT = (By.ID, 'Password')
    AUTH_BUTTON = (By.ID, 'authbtn')
    ENTER_BUTTON_XPATH = '//*[@id="loginForm"]/input[1]'
    LINK_TO_ONLINE_SERVICES_PAGE = (By.XPATH, '//*[@id="invest-moscow-app"]/div[2]/div[3]/div[1]/nav/a[5]')
    LOGIN = 'ilyaaanichkin@upt24.ru'
    PASSWORD = 'lgRtaSnz$1'
    HEADER_USER_NAME = (By.XPATH, '//*[@id="auth-bt"]/a/span')
    HEADER_USER_NAME_TEXT = 'Аничкин И. В.'
    

    def get_title(self):
        '''Функция получения тайтла страницы'''
        
        return self.driver.title


    def open_main_page(driver, base_url):
        page = MainPage(driver, base_url)
        page.get()
        return page

    def get_header_user_name(self):
        '''Функция ожидания появления элемента при авторизации'''

        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainPage.HEADER_USER_NAME))
        return header.text

    def go_to_online_services_page(self):
        '''Функция перехода в раздел Онлайн сервисы'''
        link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPage.LINK_TO_ONLINE_SERVICES_PAGE))
        link.click()
        self.driver.save_screenshot(r"C:\\Users\Влад\Desktop\Skrins\test6.png")

    def login(self):
        '''Функция для ввода логина и пароля'''

        login_pic = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPage.LOGIN_PIC))
        login_pic.click()
        login_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPage.LOGIN_INPUT))
        login_input.send_keys(MainPage.LOGIN)
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPage.PASSWORD_INPUT))
        password_input.send_keys(MainPage.PASSWORD)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot")
        self.get_clicable_by_xpath(self.ENTER_BUTTON_XPATH).click()
        

    

        
        
