import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage
import allure



class IndustriesPage(BasePage):

    PATH = '/industries'
    TITLE = 'Промышленности - Инвестиционный портал Москвы'
    MOSCOW_TECHNICAL_SCHOOL = (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]')
    BANNER_TECH_SCOOL = (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[2]/div/div[2]/img')
    PRODUCTION = (By.XPATH, '//*[@id="invest-moscow-app"]/div[13]')
    MOSPROM_BANNER = (By.CSS_SELECTOR, '#invest-moscow-app > a')
    BANK = (By.XPATH, '//*[@id="invest-moscow-app"]/div[20]')
    INDUSTRIES_BANNER = (By.CSS_SELECTOR, '#invest-moscow-app > div.industries-loans-banner')
    SUPPORT_EXPORT_CONTENT = (By.CSS_SELECTOR, '#invest-moscow-app > div.industries-export-banner.industries-tab-link')
    ANALYTICAL_MATERIALS = (By.XPATH, '//*[@id="invest-moscow-app"]/div[27]')


    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title


    def check_blocks(self):
        with allure.step('Проверка наличия блока МТШ'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.MOSCOW_TECHNICAL_SCHOOL))
        with allure.step('Проверка наличия баннера МТШ'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.BANNER_TECH_SCOOL))
        with allure.step('Проверка наличия блока подбора промышленных площадок'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.PRODUCTION))
        with allure.step('Проверка наличия моспром баннера'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.MOSPROM_BANNER))
        with allure.step('Проверка наличия блока Банк технологий'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.BANK))
        with allure.step('Проверка наличия баннера льготных займов и компенсаций'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.INDUSTRIES_BANNER))
        with allure.step('Проверка наличия блока поддержки экспортеров'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.SUPPORT_EXPORT_CONTENT))
        with allure.step('Проверка наличия блока аналитических материалов'):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.ANALYTICAL_MATERIALS))
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot")
        