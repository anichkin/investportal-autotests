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

    PATH = '/new-tenders'
    TITLE = 'Торги.Имущество - Инвестиционный портал Москвы'
    OBJECT_TYPE_XPATH = '//*[@id="uid-portal"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]'
    TRADE_TYPE_XPATH = '//*[@id="uid-portal"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]'

    def select_object_types(self, types: Iterable[str]) -> None:
        object_filter = Filter(self, NewTendersPage.OBJECT_TYPE_XPATH)
        object_filter.select(types)

    def select_trade_types(self, types: Iterable[str]) -> None:
        trade_filter = Filter(self, NewTendersPage.TRADE_TYPE_XPATH)
        trade_filter.select(types)