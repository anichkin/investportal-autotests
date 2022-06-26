from autotests.pages.base_page import BasePage


class MyTenderPage(BasePage):
    PATH = '/lk/tenders/applications'
    APPLICATION_TAB_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[1]/a'
    APPLICATION_TAB = 'ЗАЯВКИ'
    CONTRACT_TAB_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[2]/a'
    CONTRACT_TAB = 'ДОГОВОРЫ'
    AMOUNT_CHECK = '//*[text()[contains(.,"результатов")]]'
    CONTRACT_AMOUNT = 'Всего 0 результатов'
    FAVORITE_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[3]/a'
    FAVORITE = 'ИЗБРАННЫЕ ТОРГИ'
    FAVORITE_AMOUNT = 'Всего 4 результатов'
    FIRST_FAVORITE_TENDER = '#app > div.app > div.uid-lk-main > div > div:nth-child(2)'
    TENDER_NAME_XPATH = '//*[@id="app"]/div[3]/div[4]/div/div[2]/div/div[1]/div[2]'
    TENDER_NAME = '42.2 М 2 НЕЖИЛОЕ ПОМЕЩЕНИЕ В АРЕНДУ'
    MY_FILTERS_TAB_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[4]/a'
    MY_FILTERS_TAB = 'МОИ ФИЛЬТРЫ'
    FIRST_FILTER = '//*[@id="app"]/div[3]/div[4]/div/div[2]/div'
    FIRST_FILTER_NAME_XPATH = '//*[@id="app"]/div[3]/div[4]/div/div[2]/div/div[1]/div[1]'
    FIRST_FILTER_NAME = 'ТЕСТОВЫЙ ФИЛЬТР'
    FILTERS_AMOUNT = 'Всего 2 результатов'
    COMPARE_TAB_XPATH = '//*[@id="app"]/div[3]/div[2]/div/div/div[3]/div[5]/a'
    COMPARE_TAB = 'СРАВНЕНИЕ ОБЪЕКТОВ'
    COMPARE_AREA = '//*[@id="app"]/div[3]/div[4]/div/div[2]/div/div[2]'
    FIRST_TENDER_NAME_XPATH = '//*[@id="app"]/div[3]/div[4]/div/div[2]/div/div[1]/div/div[1]/div'
    FIRST_TENDER_NAME = '634 М2 ПРАВО РАЗМЕЩЕНИЯ НЕКАПИТАЛЬНОГО ОБЪЕКТА'
    COMPARE_AMOUNT = 'Всего 3 результатов'
