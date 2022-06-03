from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import allure


class NMPCalculator(BasePage):

    PATH = '/online-services/navigator-support-measures/detail/a2202ea2-c515-4d24-af5e-bdfce59bf546'
    TITLE = 'Навигатор мер поддержки - Инвестиционный портал Москвы'
    HEADER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[1]/div/div[1]'
    HEADER = 'Инвестиционный проект по созданию мест приложения труда'
    SUBTITLE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[1]/div/div[2]'
    SUBTITLE = 'Освобождение застройщика многоквартирного дома от платы за изменение вида разрешенного использования земельного участка при инвестиции в строительство мест приложения труда.'
    CALCULATOR_BUTTON = (By.XPATH, '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[3]/div[2]/div[2]/button')
    DISTRICT = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[2]'
    DISTRICT_SELECT = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/div[2]/div/span[3]'
    SQUARE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div[4]/div/div/input'
    SQUARE = '5678'
    PURPOSE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div[5]/div/div[2]/div[1]'
    HOSTEL_PURPOSE = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div[5]/div/div[2]/div[2]/div/span[2]'
    PROGRESS_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div[6]/div/div/input'
    PROGRESS = '25'
    CALULATE_BUTTON = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[3]/button'
    FIRST_CALC_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[4]/div/div[3]/div[1]'
    FIRST_CALC = 'Предельный срок реализации проекта по созданию места приложения труда, лет'
    FIRST_CALC_NUMBER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[4]/div/div[3]/div[2]/div'
    FIRST_CALC_NUMBER = '3'
    SECOND_CALC_NUMBER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[4]/div/div[3]/div[4]/div'
    SECOND_CALC_NUMBER = '269,7'
    THIRD_CALC_NUMBER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[4]/div/div[3]/div[6]/div'
    THIRD_CALC_NUMBER = '354,7'
    FORTH_CALC_NUMBER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div[2]/div[3]/div/div[4]/div/div[3]/div[8]/div'
    FORTH_CALC_NUMBER = '202,3'




    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title



    def check_calculator(self):
        '''Функция проверки кнопки калькулятор'''

        calculator = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(NMPCalculator.CALCULATOR_BUTTON))
        calculator.click()


    def check_calculations(self):
        district = self.get_visible_by_xpath(NMPCalculator.DISTRICT)
        district.click()
        select_district = self.get_clicable_by_xpath(NMPCalculator.DISTRICT_SELECT)
        select_district.click()
        square_input = self.get_visible_by_xpath(NMPCalculator.SQUARE_XPATH)
        square_input.send_keys(NMPCalculator.SQUARE)
        purpose = self.get_visible_by_xpath(NMPCalculator.PURPOSE_XPATH)
        purpose.click()
        select_purpose = self.get_visible_by_xpath(NMPCalculator.HOSTEL_PURPOSE)
        select_purpose.click()
        progress = self.get_visible_by_xpath(NMPCalculator.PROGRESS_XPATH)
        progress.send_keys(NMPCalculator.PROGRESS)
        self.get_clicable_by_xpath(NMPCalculator.CALULATE_BUTTON).click()

