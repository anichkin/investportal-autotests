from typing import Iterable, List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage


class Filter():

    def __init__(self, page: BasePage, xpath: str) -> None:
        self.page = page
        self.element = self.page.get_clicable_by_xpath(xpath)
        self.element.click()
        self.labels = {}
        for elem in self.element.find_elements(By.TAG_NAME, 'label'):
            text = elem.find_element(By.XPATH, './span[2]').text
            self.labels[text] = elem.find_element(By.XPATH, './span[1]')

    def select(self, choices: List[str]) -> None:
        for choice in choices:
            self.labels[choice].click()


class NewTendersPage(BasePage):

    PATH = '/tenders'
    TITLE = 'Торги.Имущество - Инвестиционный портал Москвы'
    OBJECT_TYPE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div/div'
    TRADE_TYPE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div'
    SEARCH_BUTTON = '.uid-btn_size_large > div'
    TENDER_AREA = '//div[@id="uid-portal"]/div/div/div[3]/div/h2'
    FIRST_NEW_TENDER = '.list:nth-child(3) .uid-tenders-card:nth-child(1) > .uid-tenders-card__main'
    SECOND_NEW_TENDER = '.list:nth-child(3) .uid-tenders-card:nth-child(2) > .uid-tenders-card__main'
    THIRD_NEW_TENDER = '.list:nth-child(3) .uid-tenders-card:nth-child(3) > .uid-tenders-card__main'
    FIRST_POPULAR_TENDER = '.list:nth-child(4) .uid-tenders-card:nth-child(1) .uid-text-small > span'
    SECOND_POPULAR_TENDER = '.list:nth-child(4) .uid-tenders-card:nth-child(2) > .uid-tenders-card__main'
    THIRD_POPULAR_TENDER = '.list:nth-child(4) .uid-tenders-card:nth-child(3) > .uid-tenders-card__main'
    FIRST_SEARCH_RESULT_TENDER1 = '.uid-mb-0 .uid-tenders-card__main-left-col'
    FIRST_SEARCH_RESULT_TENDER2 = '.uid-tenders-card:nth-child(3) > .uid-tenders-card__main'
    ALL_OBJECT_BUTTON = '.list:nth-child(2) .uid-btn > div'
    WIDE_FILTER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[2]/div/div/div/div[1]'
    WIDE_FILTER = 'Расширенный поиск'
    SQUARE = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h1/span'
    TENDER_NAME = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h1/text()'
    MAP = '//*[@id="map"]'



    def select_object_types(self, types: Iterable[str]) -> None:
        object_filter = Filter(self, NewTendersPage.OBJECT_TYPE_XPATH)
        object_filter.select(types)

    def select_trade_types(self, types: Iterable[str]) -> None:
        trade_filter = Filter(self, NewTendersPage.TRADE_TYPE_XPATH)
        trade_filter.select(types)