from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage
import allure


class MainPage(BasePage):

    PATH = ''
    TITLE = 'Главная - Инвестиционный портал Москвы'
    LOGIN_PIC = (By.CSS_SELECTOR, '.uid-mr-8')
    LOGIN_INPUT = (By.ID, 'Login')
    PASSWORD_INPUT = (By.ID, 'Password')
    AUTH_BUTTON = (By.ID, 'authbtn')
    ENTER_BUTTON_XPATH = '.button_style_login'
    LINK_TO_ONLINE_SERVICES_PAGE = (By.XPATH, '//*[@id="invest-moscow-app"]/div[2]/div[3]/div[1]/nav/a[5]')
    LOGIN = 'authorization_test@upt24.ru'
    PASSWORD = '#eZam5rK'
    HEADER_USER_NAME = (By.XPATH, '//*[@id="uid-header-target"]/div/div/div[2]/div/div[2]/div[1]/div/span')
    HEADER_USER_NAME_TEXT = 'Авторизация Т.'
    NOTIFICATION = (By.XPATH, '//*[@id="uid-header-target"]/div/div/div[2]/div/div[1]/div[1]/div')
    LOGOUT = (By.XPATH, '//*[@id="logout"]')
    HEADER_USER_NAME_LOGOUT = (By.CLASS_NAME, 'header_user_name auth-user-name auth-user-name_hidden')


    def get_title(self):
        '''Функция получения тайтла страницы'''
        
        return self.driver.title


    def open_main_page(driver, base_url):
        page = MainPage(driver, base_url)
        page.get()
        return page

    def get_header_user_name(self):
        '''Функция ожидания появления элемента при авторизации'''

        header = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(MainPage.HEADER_USER_NAME))
        return header.text

    def authorization_check(self):
        check = WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located(MainPage.NOTIFICATION)))

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
        enter = self.get_clicable_by_css(self.ENTER_BUTTON_XPATH)
        enter.click()

    def logout(self):
        menu = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(MainPage.LOGIN_PIC))
        menu.click()
        logout = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(MainPage.LOGOUT))
        logout.click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(MainPage.HEADER_USER_NAME_LOGOUT))

        

    

        
        
