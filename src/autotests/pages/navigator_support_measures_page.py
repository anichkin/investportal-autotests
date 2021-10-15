from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class NMPPage(BasePage):
    
    PATH = '/online-services/navigator-support-measures'
    TITLE = 'Навигатор мер поддержки - Инвестиционный портал Москвы'
    NMP_FILTER = (By.ID, 'nsmFilters')
    SUPPORT_MEASURES = (By.ID, 'supportMeasures')
    EXPORT_BUTTON = (By.XPATH, '//*[@id="supportMeasures"]/div[1]/div[2]')





    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title

    def check_filters(self):
        '''Функция проверки отображения фильтров НМП'''

        nmp_filters = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(NMPPage.NMP_FILTER))


    def check_measures(self):
        '''Функция проверки отображения мер поддержки'''

        measures = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(NMPPage.SUPPORT_MEASURES))



    def check_export(self):
        '''Функция проверки выгрузки на странице'''

        export_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(NMPPage.EXPORT_BUTTON))
        


