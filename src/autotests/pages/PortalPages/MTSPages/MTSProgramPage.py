from autotests.pages.base_page import BasePage

class MTSProgramPage(BasePage):
    PATH = '/moscow-technical-school/programs'
    HEADER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[1]/div/div'
    HEADER = 'ОБРАЗОВАТЕЛЬНЫЕ ПРОГРАММЫ МТШ'
    SUBTITLE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[1]/div[1]'
    SUBTITLE = 'ОБРАЗОВАТЕЛЬНЫЕ ПРОГРАММЫ'
    PROGRAM1 = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[1]/div[2]'
    PROGRAM2 = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[1]/div[3]'
    PROGRAM3 = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[1]/div[4]'
    PROGRAM4 = '//*[@id="uid-portal"]/div/div[1]/div[3]/div[4]/div/div[1]/div[5]'

