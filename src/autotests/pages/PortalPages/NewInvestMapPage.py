from autotests.pages.base_page import BasePage


class NewInvestMapPage(BasePage):
    PATH = '/about-moscow/investment-map-v2/'
    TITLE = 'Инвестиционная карта - Инвестиционный портал Москвы'
    INVESTMAP_AREA = '//*[@id="invest-map"]'
    SIDEBAR_AREA = '//*[@id="uid-portal"]/div/div[1]/div[2]/div[2]/div'
    