from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndustriesPage:

    URL = 'https://investmoscow.ru/industries'
    TITLE = 'Промышленности - Инвестиционный портал Москвы'
    MOSCOW_TECHNICAL_SCHOOL = (By.XPATH)





    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver

    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title