from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NMPCalculator:

    URL = 'https://investmoscow.ru/online-services/navigator-support-measures/detail?id=9ed20a82-966b-47f1-aa77-1501d7709938#/'
    TITLE = 'Навигатор мер поддержки - Инвестиционный портал Москвы'
    CALCULATOR_BUTTON = (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[3]/div[2]/div[2]/aa')



    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver

    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title



    def check_calculator(self):
        '''Функция проверки кнопки калькулятор'''

        calculator = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_(NMPCalculator.CALCULATOR_BUTTON))
        calculator.click()

