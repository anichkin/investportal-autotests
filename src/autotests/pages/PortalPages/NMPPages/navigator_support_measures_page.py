from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage


class NMPPage(BasePage):
    
    PATH = '/online-services/navigator-support-measures'
    TITLE = 'Навигатор мер поддержки - Инвестиционный портал Москвы'
    NMP_FILTER = (By.ID, 'nsmFilters')
    SUPPORT_MEASURES = (By.ID, 'supportMeasures')
    EXPORT_BUTTON = (By.XPATH, '//*[@id="supportMeasures"]/div[1]/div[2]')
    HEADER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/h1'
    HEADER = 'Меры поддержки'
    SUBTITLE1_XPATH = '//*[contains(text(), "На нашем портале размещены меры поддержки, которые предоставляет Правительство Москвы начинающим и действующим предпринимателям. Вы можете подобрать подходящие вам субсидии, займы, гранты и налоговые льготы.")]'
    NUMBER_OF_MEASURES_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/p/span'
    NUMBER_OF_MEASURES = '158'
    MEASURES_BUTTON = '//*[@id="uid-portal"]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[3]/button[2]'
    SUPPORT_MEASURES_XPATH = '//*[@id="support-measures"]'
    FIRST_MEASURE_XPATH = '//*[@id="support-measures"]/div[2]/a[1]/div[2]'
    FIRST_MEASURE = 'Грант на развитие производства'
    SECOND_MEASURE_XPATH = '//*[@id="support-measures"]/div[2]/a[2]/div[2]'
    SECOND_MEASURE = 'Онлайн-экспорт на Tradekey.com'
    THIRD_MEASURE_XPATH = '//*[@id="support-measures"]/div[2]/a[3]/div[2]'
    THIRD_MEASURE = 'Мораторий на повышение арендной платы за земельные участки'










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
        


