from autotests.pages.base_page import BasePage


class LKPage(BasePage):

    PATH = '/lk/'
    TITLE = 'Главная - Инвестиционный портал Москвы'
    MY_TENDERS_SELECTOR = '#app > div.app > div.uid-lk-main > div > div > div.uid-home__main > div.uid-home-widgets > div:nth-child(2) > div.uid-widget__header.uid-mb-32 > div'
    MY_TENDERS = 'МОИ ТОРГИ'
    MAIN_CONTRACTS_SELECTOR = '#app > div.app > div.uid-lk-main > div > div > div.uid-home__main > div.uid-home-widgets > div:nth-child(2) > div.uid-widget__body > div:nth-child(1) > div.uid-widget-item__header > div'
    MAIN_CONTRACTS = 'ДОГОВОРЫ'
    CONTRACT_INFO_SELECTOR = '#app > div.app > div.uid-lk-main > div > div > div.uid-home__main > div.uid-home-widgets > div:nth-child(2) > div.uid-widget__body > div:nth-child(1) > div.uid-lk-zero-state > p'
    CONTRACT_INFO = 'У вас нет ещё ни одного договора.'
    MAIN_FAVORITE_TENDERS_SELECTOR = '#app > div.app > div.uid-lk-main > div > div > div.uid-home__main > div.uid-home-widgets > div:nth-child(2) > div.uid-widget__body > div:nth-child(2) > div.uid-widget-item__header > div'
    MAIN_FAVORITE_TENDERS = 'ИЗБРАННЫЕ ТОРГИ\n4'
    ROOM_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/a[1]/div'
    ROOM = 'НЕЖИЛОЕ ПОМЕЩЕНИЕ 2'
    CAR_PLACE_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/a[2]/div'
    CAR_PLACE = 'МАШИНО-МЕСТО 1'
    BUILDING_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/a[3]/div'
    BUILDING = 'ЗДАНИЕ 1'
    CALENDAR = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[2]/div'
    COMPARE_VIDGET_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[3]/div[1]/div'
    COMPARE_VIDGET = 'СРАВНЕНИЕ ОБЪЕКТОВ\n3'
    COMPARE_ROOM_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/a[1]/div'
    COMPARE_ROOM = 'НЕЖИЛОЕ ПОМЕЩЕНИЕ 1'
    COMPARE_CAR_PLACE_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/a[2]/div'
    COMPARE_CAR_PLACE = 'МАШИНО-МЕСТО 1'
    COMPARE_NON_CAPITAL_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[3]/div[3]/div[1]/a[3]/div'
    COMPARE_NON_CAPITAL = 'НЕКАПИТАЛЬНЫЙ ОБЪЕКТ 1'
    MY_FILTERS_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[1]/div'
    MY_FILTERS = 'МОИ ФИЛЬТРЫ'
    FILTER_NAME_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[3]/div[1]/div[1]'
    FILTER_NAME = 'ARENDA'
    FILTER_DATA_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[3]/div[1]/div[2]/div'
    FILTER_BUTTON = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/a'
    DELETE_FILTER_BUTTON = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/button'
    APPLICATION_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[5]/div[1]/div'
    APPLICATION = 'ЗАЯВКИ'
    APPLICATION_INFO_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div[5]/div[3]/p'
    APPLICATION_INFO = 'У вас не подано ещё ни одной заявки.'
    MY_APPLICATIONS_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div'
    MY_APPLICATIONS = 'МОИ ЗАЯВКИ'
    CITY_TENDERS_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div'
    CITY_TENDERS = 'ГОРОДСКИЕ ТОРГИ'
    CITY_TENDERS_INFO_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[3]/p'
    CITY_TENDERS_INFO = 'У вас не подано ещё ни одной заявки.'
    SERVICES_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div'
    SERVICES = 'УСЛУГИ'
    SERVICES_INFO_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/div[2]/div[3]/p'
    SERVICES_INFO = 'У вас не подано ещё ни одной заявки.'
    SUPPORT_MEASURES_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/div[3]/div[1]/div'
    SUPPORT_MEASURES = 'МЕРЫ ПОДДЕРЖКИ'
    SUPPORT_MEASURES_INFO_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/div[3]/div[2]/div[3]/div[3]/p'
    SUPPORT_MEASURES_INFO = 'У вас не подано ещё ни одной заявки.'
    MY_TENDERS_TAB = '//*[@id="app"]/div[3]/div[1]/div[2]/div/div[3]/div[2]/a'
    APPLICATION_TAB = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/a'
    HEADER_LK = '//*[@id="uid-header-target"]/div/div/div[2]/div/div[2]/div[1]/div/span'
    EXIT = '//*[@id="uid-header-target"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div'


    def logout_from_lk(driver, base_url):
        page = LKPage(driver, base_url)
        page.get()
        try:
            page.get_clicable_by_xpath(page.HEADER_LK).click()
        except Exception:
            driver.refresh()
            page.get_clicable_by_xpath(page.HEADER_LK).click()
        page.get_clicable_by_xpath(page.EXIT).click()
