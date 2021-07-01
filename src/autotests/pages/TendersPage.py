from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TendersPage:
    URL = 'https://investmoscow.ru/tenders'
    TITLE = 'Торги. Имущество - Инвестиционный портал Москвы'
    TENDERS = (By.XPATH, '//*[@id="invest-moscow-app"]/div[2]/div[2]/div[2]/div[1]/nav/div/a[4]')

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

    SALE_FOR_BISSNESS_ALL_OBJECTS = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[3]/ul/li[1]/a')
    URL_SALE_FOR_BISSNESS_ALL_OBJECTS = 'https://investmoscow.ru/tenders/prodazha-dlya-biznesa-vse-obekty'
    TEXT_SALE_FOR_BISSNESS_ALL_OBJECTS = 'ПРОДАЖА ДЛЯ БИЗНЕСА. ВСЕ ОБЪЕКТЫ'

    SALE_FOR_BISSNESS_PREMISES = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[3]/ul/li[2]/a')
    URL_SALE_FOR_BISSNESS_PREMISES = 'https://investmoscow.ru/tenders/prodazha-dlya-biznesa-nezhiloe-pomeshchenie'
    TEXT_SALE_FOR_BISSNESS_PREMISES = 'ПРОДАЖА ДЛЯ БИЗНЕСА. НЕЖИЛОЕ ПОМЕЩЕНИЕ'

    SALE_FOR_BISSNESS_BUILDING = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[3]/ul/li[3]/a')
    URL_SALE_FOR_BISSNESS_BUILDING = 'https://investmoscow.ru/tenders/prodazha-dlya-biznesa-zdanie'
    TEXT_SALE_FOR_BISSNESS_BUILDING = 'ПРОДАЖА ДЛЯ БИЗНЕСА. ЗДАНИЕ'

    SALE_FOR_BISSNESS_STRUCTURE = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[3]/ul/li[4]/a')
    URL_SALE_FOR_BISSNESS_STRUCTURE = 'https://investmoscow.ru/tenders/sell-structure'
    TEXT_SALE_FOR_BISSNESS_STRUCTURE = 'ПРОДАЖА ДЛЯ БИЗНЕСА. СООРУЖЕНИЕ'

    SALE_FOR_BISSNESS_NON_FINISHED = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[3]/ul/li[5]/a')
    URL_SALE_FOR_BISSNESS_NON_FINISHED = 'https://investmoscow.ru/tenders/sell-not-finished'
    TEXT_SALE_FOR_BISSNESS_NON_FINISHED = 'ПРОДАЖА ДЛЯ БИЗНЕСА. ОБЪЕКТ НЕЗАВЕРШЕННОГО СТРОИТЕЛЬСТВА'

    SALE_FOR_BISSNESS_LAND_AND_BUILDING = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[3]/ul/li[6]/a')
    URL_SALE_FOR_BISSNESS_LAND_AND_BUILDING = 'https://investmoscow.ru/tenders/prodazha-dlya-biznesa-zdanie-zemelnyj-uchastok'
    TEXT_SALE_FOR_BISSNESS_LAND_AND_BUILDING = 'ПРОДАЖА ДЛЯ БИЗНЕСА. ЗДАНИЕ+ЗЕМЕЛЬНЫЙ УЧАСТОК'

    SALE_FOR_BISSNESS_STOCK = (By.XPATH, '//*[@id="property-list"]/div/div[1]/div[3]/ul/li[7]/a')
    URL_SALE_FOR_BISSNESS_STOCK = 'https://investmoscow.ru/tenders/prodazha-dlya-biznesa-akcii-doli'
    TEXT_SALE_FOR_BISSNESS_STOCK = 'ПРОДАЖА ДЛЯ БИЗНЕСА. АКЦИИ/ДОЛИ'

    LAND_FOR_BUILDING = (By.XPATH, '//*[@id="property-list"]/div/div[2]/div[1]/ul/li/a')
    URL_LAND_FOR_BUILDING = 'https://investmoscow.ru/tenders/zemlya-pod-stroitelstvo-zemelnyj-uchastok'
    TEXT_LAND_FOR_BUILDING = 'ЗЕМЛЯ ПОД СТРОИТЕЛЬСТВО. ЗЕМЕЛЬНЫЙ УЧАСТОК'

    FOR_PEOPLE_ALL_OBJECTS = (By.XPATH, '//*[@id="property-list"]/div/div[2]/div[3]/ul/li[1]/a')
    URL_FOR_PEOPLE_ALL_OBJECTS = 'https://investmoscow.ru/tenders/dlya-zhitelej-vse-obekty'
    TEXT_FOR_PEOPLE_ALL_OBJECTS = 'ДЛЯ ЖИТЕЛЕЙ. ВСЕ ОБЪЕКТЫ'

    FOR_PEOPLE_FLAT = (By.XPATH, '//*[@id="property-list"]/div/div[2]/div[3]/ul/li[2]/a')
    URL_FOR_PEOPLE_FLAT = 'https://investmoscow.ru/tenders/dlya-zhitelej-kvartira'
    TEXT_FOR_PEOPLE_FLAT = 'ДЛЯ ЖИТЕЛЕЙ. КВАРТИРА'

    FOR_PEOPLE_ROOM = (By.XPATH, '//*[@id="property-list"]/div/div[2]/div[3]/ul/li[3]/a')
    URL_FOR_PEOPLE_ROOM = 'https://investmoscow.ru/tenders/dlya-zhitelej-komnata'
    TEXT_FOR_PEOPLE_ROOM = 'ДЛЯ ЖИТЕЛЕЙ. КОМНАТА'

    FOR_PEOPLE_PATH_OF_FLAT = (By.XPATH, '//*[@id="property-list"]/div/div[2]/div[3]/ul/li[4]/a')
    URL_FOR_PEOPLE_PATH_OF_FLAT = 'https://investmoscow.ru/tenders/dlya-zhitelej-dolya-v-kvartire'
    TEXT_FOR_PEOPLE_PATH_OF_FLAT = 'ДЛЯ ЖИТЕЛЕЙ. ДОЛЯ В КВАРТИРЕ'

    FOR_PEOPLE_LAND_IJS = (By.XPATH, '//*[@id="property-list"]/div/div[2]/div[3]/ul/li[5]/a')
    URL_FOR_PEOPLE_LAND_IJS = 'https://investmoscow.ru/tenders/dlya-zhitelej-zemlya-pod-izhs'
    TEXT_FOR_PEOPLE_LAND_IJS = 'ДЛЯ ЖИТЕЛЕЙ. ЗЕМЛЯ ПОД ИЖС'

    FOR_PEOPLE_PARKING = (By.XPATH, '//*[@id="property-list"]/div/div[2]/div[3]/ul/li[6]/a')
    URL_FOR_PEOPLE_PARKING = 'https://investmoscow.ru/tenders/dlya-zhitelej-mashino-mesta'
    TEXT_FOR_PEOPLE_PARKING = 'ДЛЯ ЖИТЕЛЕЙ. МАШИНО-МЕСТА'

    NON_STATIONARY_ALL_OBJECTS = (By.XPATH, '//*[@id="property-list"]/div/div[3]/div[1]/ul/li[1]/a')
    URL_NON_STATIONARY_ALL_OBJECTS = 'https://investmoscow.ru/tenders/nestacionarnye-obekty-vse-obekty'
    TEXT_NON_STATIONARY_ALL_OBJECTS = 'НЕСТАЦИОНАРНЫЕ ОБЪЕКТЫ. ВСЕ ОБЪЕКТЫ'

    NON_STATIONARY_ALL_OBJECTS = (By.XPATH, '//*[@id="property-list"]/div/div[3]/div[1]/ul/li[1]/a')
    URL_NON_STATIONARY_ALL_OBJECTS = 'https://investmoscow.ru/tenders/nestacionarnye-obekty-vse-obekty'
    TEXT_NON_STATIONARY_ALL_OBJECTS = 'НЕСТАЦИОНАРНЫЕ ОБЪЕКТЫ. ВСЕ ОБЪЕКТЫ'

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


    def open_tender_page(driver):
        driver.get(TendersPage.URL)
        tenders = TendersPage(driver)
        return tenders

    def open_all_project(self):
        '''Открытие всех торгов'''
        all_project = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.ALL_OBJECTS))
        all_project.click()

    def open_rent_for_bissness_all(self):
        '''Открытие всех объектов в аренде для бизнеса'''
        rent_for_bissness_all = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.RENT_FOR_BISSNESS_ALL))
        rent_for_bissness_all.click()

    def open_rent_for_bissness_room(self):
        '''Открытие нежилых помещений в аренде для бизнеса'''
        rent_for_bissness_room = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.RENT_FOR_BISSNESS_ROOM))
        rent_for_bissness_room.click()

    def open_rent_for_bissness_building(self):
        '''Открытие зданий в аренде для бизнеса'''
        rent_for_bissness_building = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.RENT_FOR_BISSNESS_BUILDING))
        rent_for_bissness_building.click()

    def open_rent_for_bissness_structure(self):
        '''Открытие сооружений в аренде для бизнеса'''
        rent_for_bissness_structure = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.RENT_FOR_BISSNESS_STRUCTURE))
        rent_for_bissness_structure.click()

    def return_to_tenders(self):
        tenders = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(TendersPage.TENDERS))
        tenders.click()

    def open_sale_for_bissness_all_objects(self):
        sale_for_bissness_all_objects = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.SALE_FOR_BISSNESS_ALL_OBJECTS))
        sale_for_bissness_all_objects.click()

    def open_sale_for_bissness_premises(self):
        sale_for_bissness_premises = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.SALE_FOR_BISSNESS_PREMISES))
        sale_for_bissness_premises.click()

    def open_sale_for_bissness_building(self):
        sale_for_bissness_building = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.SALE_FOR_BISSNESS_BUILDING))
        sale_for_bissness_building.click()

    def open_sale_for_bissness_structure(self):
        sale_for_bissness_structure = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.SALE_FOR_BISSNESS_STRUCTURE))
        sale_for_bissness_structure.click()

    def open_sale_for_bissness_non_finished(self):
        sale_for_bissness_non_finished = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.SALE_FOR_BISSNESS_NON_FINISHED))
        sale_for_bissness_non_finished.click()

    def open_sale_for_bissness_land_and_building(self):
        sale_for_bissness_land_and_building = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.SALE_FOR_BISSNESS_LAND_AND_BUILDING))
        sale_for_bissness_land_and_building.click()

    def open_sale_for_bissness_stock(self):
        sale_for_bissness_stock = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.SALE_FOR_BISSNESS_STOCK))
        sale_for_bissness_stock.click()

    def open_land_for_building(self):
        land_for_building = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.LAND_FOR_BUILDING))
        land_for_building.click()

    def open_for_people_all_objects(self):
        for_people_all_objects = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.FOR_PEOPLE_ALL_OBJECTS))
        for_people_all_objects.click()

    def open_for_people_flat(self):
        for_people_flat = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.FOR_PEOPLE_FLAT))
        for_people_flat.click()

    def open_for_people_room(self):
        for_people_room = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.FOR_PEOPLE_ROOM))
        for_people_room.click()

    def open_for_people_path_of_flat(self):
        for_people_path_of_flat = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.FOR_PEOPLE_PATH_OF_FLAT))
        for_people_path_of_flat.click()

    def open_for_people_land_ijs(self):
        for_people_land_ijs = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.FOR_PEOPLE_LAND_IJS))
        for_people_land_ijs.click()

    def open_for_people_parking(self):
        for_people_parking = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TendersPage.FOR_PEOPLE_PARKING))
        for_people_parking.click()

