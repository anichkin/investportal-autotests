from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InvestmentMapPage:

    URL = 'https://investmoscow.ru/about-moscow/investment-map'
    TITLE = 'Инвестиционная карта Москвы - Инвестиционный портал Москвы'
    MAP = (By.ID, 'investment-map')



    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver

    def get_title(self):
        '''Функция получения тайтла страницы'''
        
        return self.driver.title


    def check_map(self):
        '''Проверка отображения карты на странице'''

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(InvestmentMapPage.MAP))