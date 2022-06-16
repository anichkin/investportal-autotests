from autotests.pages.base_page import BasePage

class DGPSubjectReestrPage(BasePage):
    PATH = '/Doutree2/ExternalApp/SubjectRegistry.aspx'
    HEADER_XPATH = '//*[@id="app"]/div[1]/div[2]/div/h1'
    HEADER = 'РЕЕСТР СУБЪЕКТОВ ИНВЕСТИЦИОННОЙ ДЕЯТЕЛЬНОСТИ'
    CARDS_AREA_XPATH = '//*[@id="app"]/div[1]/div[2]/div/div[3]'
    FIRST_CARD = '//*[@id="app"]/div[1]/div[2]/div/div[3]/div[1]'
    FILTER_AREA = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div'
    CHECKBOX = '.column:nth-child(1) .checkbox__label'
    ENTER_BUTTON = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[3]/div[2]/button[3]'
    REQUEST_FOR_DOC_XPATH = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div/button'
    REQUEST_FOR_DOC = 'Запросить выписки'
    DOWNLOAD_BUTTON_XPATH = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/button'
    DOWNLOAD_BUTTON = 'Скачать'
    PROPERTY_TAB = '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/ul/li[3]/a'
    FIRST_PROPERTY = '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]'





