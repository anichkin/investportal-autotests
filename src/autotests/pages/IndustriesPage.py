from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage



class IndustriesPage(BasePage):

    PATH = '/industries'
    TITLE = 'Промышленности - Инвестиционный портал Москвы'
    MOSCOW_TECHNICAL_SCHOOL = (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]')
    BANNER_TECH_SCOOL = (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[2]/div/div[2]/img')
    PRODUCTION = (By.XPATH, '//*[@id="invest-moscow-app"]/div[13]')
    PROM_BANNER = (By.XPATH, '//*[@id="invest-moscow-app"]/div[15]/div[2]/div/h4')
    BANK = (By.XPATH, '//*[@id="invest-moscow-app"]/div[20]')
    INDUSTRIES_BANNER = (By.XPATH, '//*[@id="invest-moscow-app"]/div[22]/div[2]/div/h4')
    EVOLUTION_CONTENT = (By.XPATH, '//*[@id="invest-moscow-app"]/div[23]/div')
    ANALYTICAL_MATERIALS = (By.XPATH, '//*[@id="invest-moscow-app"]/div[27]')

    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title

        
    def check_blocks(self):
        '''Проверка отображения всех блоков на странице'''

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.MOSCOW_TECHNICAL_SCHOOL))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.BANNER_TECH_SCOOL))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.PRODUCTION))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.PROM_BANNER))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.BANK))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.INDUSTRIES_BANNER))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.EVOLUTION_CONTENT))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IndustriesPage.ANALYTICAL_MATERIALS))
        