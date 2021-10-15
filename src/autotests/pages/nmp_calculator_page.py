from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class NMPCalculator(BasePage):

    PATH = '/online-services/navigator-support-measures/detail?id=60f55bcb-c563-4858-884f-dadfeb0ba954#/'
    TITLE = 'Навигатор мер поддержки - Инвестиционный портал Москвы'
    CALCULATOR_BUTTON = (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[3]/div[2]/div[2]/aa')




    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title



    def check_calculator(self):
        '''Функция проверки кнопки калькулятор'''

        calculator = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_(NMPCalculator.CALCULATOR_BUTTON))
        calculator.click()
