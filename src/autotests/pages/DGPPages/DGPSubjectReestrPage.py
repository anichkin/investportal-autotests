from autotests.pages.base_page import BasePage

class DGPSubjectReestrPage(BasePage):
    PATH = '/Doutree2/ExternalApp/SubjectRegistry.aspx'
    HEADER_XPATH = '//*[@id="app"]/div[1]/div[2]/div/h1'
    HEADER = 'РЕЕСТР СУБЪЕКТОВ ИНВЕСТИЦИОННОЙ ДЕЯТЕЛЬНОСТИ'
    CARDS_AREA = '#app > div.app-wrapper > div.uid-wrapper.flex-grow-1 > div > div.cards'
    FIRST_CARD = '#app > div.app-wrapper > div.uid-wrapper.flex-grow-1 > div > div.cards > div:nth-child(1)'
    FILTER_AREA = 'rect:nth-child(2)'
    CHECKBOX = '.column:nth-child(1) .checkbox__label'
    ENTER_BUTTON = '#app > div.app-wrapper > div.uid-wrapper.flex-grow-1 > div > form > div.filter-footer > div.filter-footer-right > button.uid-btn.uid-btn_main.uid-btn_size_small.uid-ml-32'
    REQUEST_FOR_DOC_CSS = '#app > div.app-wrapper > div.uid-wrapper.flex-grow-1 > div > div.layout > div.content > div.short-info.uid-pa-24 > div.short-info-statement > div > div.short-info-statement-button > button'
    REQUEST_FOR_DOC = 'Запросить ЕГРЮЛ'
    DOWNLOAD_BUTTON_CSS = '#app > div.app-wrapper > div.uid-wrapper.flex-grow-1 > div > div.layout > div.content > div.short-info.uid-pa-24 > div.short-info-statement > div > div.download-files > button:nth-child(1)'
    DOWNLOAD_BUTTON = 'Скачать выписку'
    PROPERTY_TAB = '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/ul/li[3]/a'
    FIRST_PROPERTY = '//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]'





