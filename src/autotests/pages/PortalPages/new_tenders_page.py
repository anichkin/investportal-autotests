from typing import Iterable, List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from autotests.pages.base_page import BasePage
import time


class Filter():

    def __init__(self, page: BasePage, xpath: str) -> None:
        self.page = page
        self.element = self.page.get_clicable_by_xpath(xpath)
        self.element.click()
        time.sleep(1)
        self.labels = {}
        for elem in self.element.find_elements(By.TAG_NAME, 'label'):
            text = elem.find_element(By.XPATH, './span[2]').text
            self.labels[text] = elem.find_element(By.XPATH, './span[1]')

    def select(self, choices: List[str]) -> None:
        for choice in choices:
            self.labels[choice].click()


class NewTendersPage(BasePage):

    PATH = '/tenders'
    TITLE = 'Торги. Имущество от города - Инвестиционный портал Москвы'
    OBJECT_TYPE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div/div'
    TRADE_TYPE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div'
    SALE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/label[2]/span[2]'
    SEARCH_BUTTON = '.uid-btn_size_large > div'
    TENDER_AREA = '//div[@id="uid-portal"]/div/div/div[3]/div/h2'
    FIRST_NEW_TENDER = '.list:nth-child(3) .uid-tenders-card:nth-child(1) > .uid-tenders-card__main'
    SECOND_NEW_TENDER = '.list:nth-child(3) .uid-tenders-card:nth-child(2) > .uid-tenders-card__main'
    THIRD_NEW_TENDER = '.list:nth-child(3) .uid-tenders-card:nth-child(3) > .uid-tenders-card__main'
    FIRST_POPULAR_TENDER = '.list:nth-child(4) .uid-tenders-card:nth-child(1) .uid-text-small > span'
    SECOND_POPULAR_TENDER = '.list:nth-child(4) .uid-tenders-card:nth-child(2) > .uid-tenders-card__main'
    THIRD_POPULAR_TENDER = '.list:nth-child(4) .uid-tenders-card:nth-child(3) > .uid-tenders-card__main'
    FIRST_SEARCH_RESULT_TENDER1 = '.uid-mb-0 .uid-tenders-card__main-left-col'
    COLLAPSE_TENDERS = '.uid-mb-40:nth-child(3) > .uid-group-card__collapse span'
    FIRST_COLLAPSE_TENDER = '..uid-group-card__body > .uid-tenders-card:nth-child(1) .uid-tenders-card__main-left-col'
    FIRST_SEARCH_RESULT_TENDER2 = '.uid-tenders-card:nth-child(3) > .uid-tenders-card__main'
    ALL_OBJECT_BUTTON = '.list:nth-child(2) .uid-btn > div'
    ALL_OBJECT_BUTTON_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div/div/button'
    WIDE_FILTER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[1]'
    WIDE_FILTER_XPATH_2 = '//*[@id="uid-portal"]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/div'
    WIDE_FILTER = 'Показать фильтр'
    SQUARE = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h1/span'
    TENDER_NAME = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h1/text()'
    MAP = '//*[@id="map"]'
    DOCUMENT_BUTTON = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div/div/div[1]/button'
    DOCUMENT_BUTTON_2 = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[1]/button'
    OBJECT_DOCUMENT = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div/div[1]/div/div[2]'
    OBJECT_DOCUMENT_2 = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[2]'
    TENDER_DOCUMENT = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[2]'
    TENDER_DOCUMENT_2 = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]'
    SUBJECT_TABS = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div'
    SIMULAR_OBJECTS = '//*[@id="uid-portal"]/div/div[1]/div[3]/div/div'
    EVENTS = '//*[@id="uid-portal"]/div/div[1]/div[4]/div[1]'
    NAVIGATION = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]'



    def select_object_types(self, types: Iterable[str]) -> None:
        object_filter = Filter(self, NewTendersPage.OBJECT_TYPE_XPATH)
        object_filter.select(types)

    def select_trade_types(self, types: Iterable[str]) -> None:
        trade_filter = Filter(self, NewTendersPage.TRADE_TYPE_XPATH)
        trade_filter.select(types)