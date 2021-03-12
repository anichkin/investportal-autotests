from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AboutMoscowPage:

    URL = 'https://investmoscow.ru/about-moscow'
    TITLE = 'О Москве - Инвестиционный портал Москвы'
    ECONOMICS = {
            'tab': (By.ID, 'economics-tab'),
            'info': (By.ID, 'nav-economics')
        }
    INVESTMENTS = {
            'tab': (By.ID, 'investments-tab'),
            'info': (By.ID, 'nav-investments')
        }
    FINANCE = {
            'tab': (By.ID, 'finance-tab'),
            'info': (By.ID, 'nav-finance')
        }
    BUSINESS = {
            'tab': (By.ID, 'business-tab'),
            'info': (By.ID, 'nav-business')
        }
    TRANSPORT = {
            'tab': (By.ID, 'transport-tab'),
            'info': (By.ID, 'nav-transport')
        }
    LIVES = {
            'tab': (By.ID, 'lives-tab'),
            'info': (By.ID, 'nav-lives')
        }
    ECOLOGY = {
            'tab': (By.ID, 'ecology-tab'),
            'info': (By.ID, 'nav-ecology')
        }

    DETAILS_BTN = (By.XPATH, '/html/body/div[1]/div[8]/a[2]')



    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver


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

    



