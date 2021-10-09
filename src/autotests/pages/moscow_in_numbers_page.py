from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class MoscowInNumberPage(BasePage):

    PATH = '/about-moscow/moscow-in-numbers'
    TITLE = 'Москва в цифрах - Инвестиционный портал Москвы'
    ECONOMIC = (By.ID, 'economic')
    ECONOMIC_INFO = (By.XPATH, '//*[@id="mm-0"]/div[8]/div[3]')
    INVESTITION = (By.ID, 'investition')
    INVESTITION_INFO = (By.XPATH, '//*[@id="mm-0"]/div[8]/div[5]')
    FINANSE = (By.ID, 'finance')
    FINANSE_INFO = (By.XPATH, '//*[@id="mm-0"]/div[8]/div[7]')
    BUSINES = (By.ID, 'busines')
    BUSINES_INFO = (By.XPATH, '//*[@id="mm-0"]/div[8]/div[9]')
    TRANSPORT = (By.ID, 'transport')
    TRANSPORT_INFO = (By.XPATH, '//*[@id="mm-0"]/div[8]/div[11]')
    LIVE = (By.ID, 'live')
    LIVE_INFO = (By.XPATH, '//*[@id="mm-0"]/div[8]/div[13]')
    ECOLOGY = (By.ID, 'ecology')
    ECOLOGY_INFO = (By.XPATH, '//*[@id="mm-0"]/div[8]/div[15]')
    ECONOMIC_NAV = (By.XPATH, '//*[@id="myScrollspy"]/ul/li[1]/a')
    INVESTITION_NAV = (By.XPATH, '//*[@id="myScrollspy"]/ul/li[2]/a')
    FINANSE_NAV = (By.XPATH, '//*[@id="myScrollspy"]/ul/li[3]/a')
    BUSINES_NAV = (By.XPATH, '//*[@id="myScrollspy"]/ul/li[4]/a')
    TRANSPORT_NAV = (By.XPATH, '//*[@id="myScrollspy"]/ul/li[5]/a')
    LIVE_NAV = (By.XPATH, '//*[@id="myScrollspy"]/ul/li[6]/a')
    ECOLOGY_NAV = (By.XPATH, '//*[@id="myScrollspy"]/ul/li[7]/a')
    DOCS_NAV = (By.XPATH, '//*[@id="myScrollspy"]/ul/li[8]/a')
    PODPISKA = (By.XPATH, '//*[@id="sticky-wrapper"]/div/div/div/div[1]/a')
    DOWNLOAD_BROCHURE = (By.XPATH, '//*[@id="sticky-wrapper"]/div/div/div/div[2]/a')


    def get_title(self):
        '''Функция получения тайтла страницы'''
        
        return self.driver.title 
        

    def check_blocks_and_menu(self):
        '''Получаем id элементов и id информации'''
        
        economic = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.ECONOMIC_NAV))
        economic.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.ECONOMIC))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.ECONOMIC_INFO))
        investition = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.INVESTITION_NAV))
        investition.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.INVESTITION))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.INVESTITION_INFO))
        finance = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.INVESTITION_NAV))
        finance.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.FINANSE))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.FINANSE_INFO))
        busines = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.BUSINES_NAV))
        busines.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.BUSINES))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.BUSINES_INFO))
        transport = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.TRANSPORT_NAV))
        transport.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.TRANSPORT))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.TRANSPORT_INFO))
        live = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.LIVE_NAV))
        live.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.LIVE))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.LIVE_INFO))
        ecology = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.ECOLOGY_NAV))
        ecology.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.ECOLOGY))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MoscowInNumberPage.ECOLOGY_INFO))
        docs = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.DOCS_NAV))
        docs.click()
       


    def check_podpiska(self):
        '''Проверяем подписку'''

        podpiska = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.PODPISKA))
        podpiska.click()



    def check_brochure(self):
        '''Проверяем кнопку Скачать брошюру'''

        brochure = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MoscowInNumberPage.DOWNLOAD_BROCHURE))
        brochure.click()