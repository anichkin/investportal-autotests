from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class PodpiskaInwestDigestPage(BasePage):

    PATH = '/online-services/podpiska-inwest-digest'
    TITLE = 'Подписка инвестиционный дайджест - Инвестиционный портал Москвы'


    def get_title(self):
        '''Функция получения тайтла страницы'''
        
        return self.driver.title 