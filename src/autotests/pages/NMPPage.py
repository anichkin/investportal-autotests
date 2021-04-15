from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NMPPage:
    URL = 'https://investmoscow.ru/online-services/navigator-support-measures'
    TITLE = 'Навигатор мер поддержки - Инвестиционный портал Москвы'
    ARENDA = (By.CSS_SELECTOR, '.nsm-filters-main > .nsm-filter:nth-child(2) .nsm-label-oval-checkbox:nth-child(1) > span')
    AUTORITY =(By.XPATH, '//*[@id="vs1__combobox"]/div[1]/input')

    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver

    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title

    def check_elements(self):
        '''Функция элементов на страници НМП'''

        arenda_check = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(NMPPage.ARENDA))
        arenda_check.click()
       # autority_check = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(NMPPage.AUTORITY))
        autority_check = Select(self.driver.find_element_by_xpath('//*[@id="vs1__combobox"]/div[1]'))
        autority_check.select_by_value('Департамент городского имущества города Москвы')


