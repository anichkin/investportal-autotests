from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage

class DGPMosInvestorPage(BasePage):
    PATH = '/Doutree2/MoscowInvestorAppeals/Index.aspx'
    URL = 'https://dgp.investmoscow.ru/'
    TAB_XPATH = '//a[contains(text(),"Реестр обращений (Московский инвестор)")]'
    TAB = 'Реестр обращений (Московский инвестор)'
    MESSAGES_AREA = '//*[@id="complaints"]/tbody'
    FIRST_MESSAGE = '//*[@id="complaints"]/tbody/tr[1]'
    COMMON_INFO_XPATH = '//*[@id="headingThree1"]/h5/button'
    COMMON_INFO = 'Общие сведения'
