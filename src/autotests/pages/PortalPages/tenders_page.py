from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage

class TendersPage(BasePage):


    PATH = '/tenders'
    TITLE = 'Торги. Имущество - Инвестиционный портал Москвы'



    def get_title(self):
        '''Функция получения тайтла страницы'''
        
        return self.driver.title