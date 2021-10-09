from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class OnlineServicesPage(BasePage):

    PATH = '/online-services'
    TITLE = 'Онлайн сервисы - Инвестиционный портал Москвы'


    def get_title(self):
    
        return self.driver.title