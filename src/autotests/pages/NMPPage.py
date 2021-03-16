from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NMPPage:
    URL = 'https://investmoscow.ru/online-services/navigator-support-measures'
    TITLE = 'Навигатор мер поддержки - Инвестиционный портал Москвы'

    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver

    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title
