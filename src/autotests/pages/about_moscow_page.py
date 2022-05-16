from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class AboutMoscowPage(BasePage):

    PATH = '/about-moscow'
    TITLE = 'О Москве - Инвестиционный портал Москвы'
    ECONOMICS = {
            'tab': (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[3]/div/nav/a[1]'),
            'info': (By.ID, 'nav-economics')
        }
    INVESTMENTS = {
            'tab': (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[3]/div/nav/a[2]'),
            'info': (By.ID, 'nav-investments')
        }
    FINANCE = {
            'tab': (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[1]/div/div/a[3]'),
            'info': (By.ID, 'nav-finance')
        }
    BUSINESS = {
            'tab': (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[1]/div/div/a[4]'),
            'info': (By.ID, 'nav-business')
        }
    TRANSPORT = {
            'tab': (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[1]/div/div/a[5]'),
            'info': (By.ID, 'nav-transport')
        }
    LIVES = {
            'tab': (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[1]/div/div/a[6]'),
            'info': (By.ID, 'nav-lives')
        }
    ECOLOGY = {
            'tab': (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[1]/div/div/a[7]'),
            'info': (By.ID, 'nav-ecology')
        }

    DETAILS_BTN = (By.XPATH, '//*[@id="invest-moscow-app"]/div[7]/div[3]/a')


    def get_title(self):
        '''Функция получения тайтла страницы'''
        
        return self.driver.title 


    def check_info(self, info_locator):
        try:
            info = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(info_locator))
            return True
        except:    
            return False

    def check_tab(self, tab_locator):
        '''Функция проверки табов и информации'''
        try:
            tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(tab_locator))
            tab.click()
            return True
        except:
            return False



    def check_details(self):
        '''Проверка перехода в Подробнее'''
        details = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AboutMoscowPage.DETAILS_BTN))
        details.click()

    



