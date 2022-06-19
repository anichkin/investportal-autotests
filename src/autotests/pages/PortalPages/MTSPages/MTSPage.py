from autotests.pages.base_page import BasePage

class MTSPage(BasePage):
    PATH = '/moscow-technical-school/about'
    TITLE = 'О проекте - Инвестиционный портал Москвы'
    HEADER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[1]/div/div'
    HEADER = 'ЧТО ТАКОЕ МОСКОВСКАЯ ТЕХНИЧЕСКАЯ ШКОЛА?'
    HEADER2_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div[1]/div[2]/div[1]'
    HEADER2 = 'ПРОЕКТ ПОЗВОЛИТ'
    MEMBERS_BUTTON = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div[1]/div[3]/a'


