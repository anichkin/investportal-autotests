from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OnlineServicesPage:

    URL = 'https://investmoscow.upt24.ru/'
    TITLE = 'Онлайн сервисы - Инвестиционный портал Москвы'

    def __init__(self, driver):

        self.driver = driver

    def get_title(self):
    
        return self.driver.title