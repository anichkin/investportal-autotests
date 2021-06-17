from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TendersPage:
    URL = 'https://investmoscow.ru/tenders'
    TITLE = 'Торги. Имущество - Инвестиционный портал Москвы'
    TENDERS = (By.XPATH, '//*[@id="mm-0"]/div[2]/div[2]/div[2]/div[1]/nav/div/a[4]')

    ALL_OBJECTS = (By.XPATH, '//*[@id="property-objects"]/div[1]/div[2]/a')
    URL_ALL_OBJECTS = 'https://investmoscow.ru/tenders/?AllTenders=True&PostedTenderKinds=2'
    TEXT_ALL_OBJECTS = 'ТОРГИ ГОРОДА МОСКВЫ'

    RENT_FOR_BISSNESS_ALL = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[1]/ul/li[1]/a')
    URL_RENT_FOR_BISSNESS_ALL = 'https://investmoscow.ru/tenders/arenda-dlya-biznesa-vse-obekty'
    TEXT_RENT_FOR_BISSNESS_ALL = 'АРЕНДА ДЛЯ БИЗНЕСА. ВСЕ ОБЪЕКТЫ'

    RENT_FOR_BISSNESS_ROOM = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[1]/ul/li[2]/a')
    URL_RENT_FOR_BISSNESS_ROOM = 'https://investmoscow.ru/tenders/arenda-dlya-biznesa-nezhiloe-pomeshchenie'
    TEXT_RENT_FOR_BISSNESS_ROOM = 'АРЕНДА ДЛЯ БИЗНЕСА. НЕЖИЛОЕ ПОМЕЩЕНИЕ'

    RENT_FOR_BISSNESS_BUILDING = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[1]/ul/li[3]/a')
    URL_RENT_FOR_BISSNESS_BUILDING = 'https://investmoscow.ru/tenders/arenda-dlya-biznesa-zdanie'
    TEXT_RENT_FOR_BISSNESS_BUILDING = 'АРЕНДА ДЛЯ БИЗНЕСА. ЗДАНИЕ'

    RENT_FOR_BISSNESS_STRUCTURE = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[1]/ul/li[4]/a')
    URL_RENT_FOR_BISSNESS_STRUCTURE = 'https://investmoscow.ru/tenders/rent-structure'
    TEXT_RENT_FOR_BISSNESS_STRUCTURE = 'АРЕНДА ДЛЯ БИЗНЕСА. СООРУЖЕНИЕ'

    ADDRESS = (By.XPATH, '//*[@id="filters"]/div/div[1]/div[4]/input')
    ON_MAP = (By.XPATH, '//*[@id="filters"]/div/div[2]/div[2]/a[1]')
    MORE_FILTERS = (By.XPATH, '//*[@id="more-filters"]')
    SEARCH = (By.XPATH, '//*[@id="btnSearch"]')



    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver

    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title

    def open_all_project(self):
        '''Открытие всех торгов'''

        all_project = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.ALL_OBJECTS))
        all_project.click()
        assert self.driver.current_url == TendersPage.URL_ALL_OBJECTS
        assert TendersPage.TEXT_ALL_OBJECTS == self.driver.find_element_by_xpath('//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text

    def open_rent_for_bissness(self):
        '''Открытие всех объектов в аренде для бизнеса'''
        rent_for_bissness_all = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.RENT_FOR_BISSNESS_ALL))
        rent_for_bissness_all.click()
        assert  self.driver.current_url == TendersPage.URL_RENT_FOR_BISSNESS_ALL
        assert TendersPage.TEXT_RENT_FOR_BISSNESS_ALL == self.driver.find_element_by_xpath('//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
        tenders = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.TENDERS))
        tenders.click()

        '''Открытие нежилых помещений в аренде для бизнеса'''
        rent_for_bissness_room = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.RENT_FOR_BISSNESS_ROOM))
        rent_for_bissness_room.click()
        assert self.driver.current_url == TendersPage.URL_RENT_FOR_BISSNESS_ROOM
        assert TendersPage.TEXT_RENT_FOR_BISSNESS_ROOM == self.driver.find_element_by_xpath('//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
        tenders = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.TENDERS))
        tenders.click()

        '''Открытие зданий в аренде для бизнеса'''
        rent_for_bissness_building = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.RENT_FOR_BISSNESS_BUILDING))
        rent_for_bissness_building.click()
        assert self.driver.current_url == TendersPage.URL_RENT_FOR_BISSNESS_BUILDING
        assert TendersPage.TEXT_RENT_FOR_BISSNESS_BUILDING == self.driver.find_element_by_xpath('//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
        tenders = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.TENDERS))
        tenders.click()

        '''Открытие сооружений в аренде для бизнеса'''
        rent_for_bissness_structure = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.RENT_FOR_BISSNESS_STRUCTURE))
        rent_for_bissness_structure.click()
        assert self.driver.current_url == TendersPage.URL_RENT_FOR_BISSNESS_STRUCTURE
        assert TendersPage.TEXT_RENT_FOR_BISSNESS_STRUCTURE == self.driver.find_element_by_xpath('//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
        tenders = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.TENDERS))
        tenders.click()







