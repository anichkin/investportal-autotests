from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage
import time


class MoscowInvestorPage(BasePage):
    PATH = '/business/moscow-investor'
    TITLE = 'Московский инвестор - Инвестиционный портал Москвы'
    HEADING = 'МОСКОВСКИЙ ИНВЕСТОР'
    HEADING_XPATH = '//*[@id="eiip-master__content-header"]/h1'
    SUBTITLE = 'Сервис помогает решить проблемы инвесторов и рассмотреть предложения по улучшению инвестиционного климата'
    SUBTITLE_XPATH = '//*[@id="eiip-master__content-header"]/p'
    HEADING2 = 'КАК РАБОТАЕТ СЕРВИС'
    HEADING2_XPATH = '//*[@id="invest-moscow-app"]/div[8]/h2'
    SUBTITLE2 = 'Вы направляете сообщение'
    SUBTITLE2_XPATH = '//*[@id="invest-moscow-app"]/div[8]/div/div[1]/p'
    SUBTITLE3 = 'Профильный орган исполнительной власти рассматривает сообщение'
    SUBTITLE3_XPATH = '//*[@id="invest-moscow-app"]/div[8]/div/div[3]/p'
    HEADING3 = 'СООБЩЕНИЕ О ПРОБЛЕМЕ'
    HEADING3_XPATH = '//*[@id="invest-moscow-app"]/div[9]/h2'

    CLASSIFICATOR_BUTTON = '//*[@id="eiip-master__content-header"]/div[3]/a'
    LAND = 'Земля'
    LAND_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[2]/div[1]/div[1]'
    LAND_CATEGORY1 = 'Предоставление льгот'
    LAND_CATEGORY1_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[1]/div/span'
    PROBLEM_36 = 'Отсрочка арендных платежей за земельный участок в связи с COVID-19 (Федеральный закон от 01.04.2020 № 98-ФЗ): получен отказ'
    PROBLEM_36_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[1]/ul/li/a'
    LAND_CATEGORY2 = 'Аренда/выкуп'
    LAND_CATEGORY2_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[2]/div/span'
    PROBLEM_38 = 'Продление договора аренды земельного участка в связи с COVID-19 (Федеральный закон Российской Федерации от 01.04.2020 № 98-ФЗ): возникла проблема'
    PROBLEM_38_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[2]/ul/li[1]/a'
    PROBLEM_1 = 'Оформление дополнительного соглашения к договору аренды земельного участка, предусматривающего проектирование и строительство (реконструкцию) объектов капитального строительства: получен отказ'
    PROBLEM_1_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[2]/ul/li[2]/a'
    PROBLEM_47 = 'Переоформление прав аренды земельного участка после завершения строительства (реконструкции) и ввода объекта в эксплуатацию: возникла проблема с оформлением прав для целей эксплуатации'
    PROBLEM_47_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[2]/ul/li[3]/a'
    PROBLEM_125 = 'У города арендован земельный участок, являющийся объектом культурного наследия/выявленным объектом культурного наследия: возникла проблема в договорных отношениях'
    PROBLEM_125_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[2]/ul/li[4]/a'
    LAND_CATEGORY3 = 'Иное'
    LAND_CATEGORY3_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[3]/div'
    PROBLEM_39 = 'Согласование границ земельного участка: получен отказ'
    PROBLEM_39_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[3]/ul/li[1]/a'
    PROBLEM_40 = 'Присвоение адреса земельному участку: получен отказ'
    PROBLEM_40_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[3]/ul/li[2]/a'
    PROBLEM_42 = 'Изменение вида разрешенного использования земельного участка: получен отказ'
    PROBLEM_42_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[3]/ul/li[3]/a'

    REAL_ESTATE = 'Недвижимость'
    REAL_ESTATE_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[2]/div[2]/div[1]'
    REAL_ESTATE_CATEGORY1 = 'Предоставление льгот'
    REAL_ESTATE_CATEGORY1_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[3]/div[1]/div/span'
    REAL_ESTATE2 = '//*[@id="invest-moscow-app"]/div[8]/div[2]/div[3]/div[2]/div/span'
    REAL_ESTATE3 = '//*[@id="invest-moscow-app"]/div[8]/div[2]/div[3]/div[3]/div'
    TENDERS = 'Торги'
    TENDERS_XPATH = '//*[@id="invest-moscow-app"]/div[9]/div[2]/div[1]/div[2]/div[2]'
    INDUSTRY_SUPPORT = 'Поддержка промышленности'
    INDUSTRY_SUPPORT_XPATH = '//*[@id="invest-moscow-app"]/div[8]/div[2]/div[1]/div[3]/div[2]'
    TAXES = '//*[@id="invest-moscow-app"]/div[8]/div[2]/div[1]/div[4]/div[2]'

    PROPOSAL = 'ЕСТЬ ПРЕДЛОЖЕНИЕ?'
    PROPOSAL_XPATH = '//*[@id="invest-moscow-app"]/div[10]/h1'
    PROPOSAL_SUBTITLE = 'Вы можете направить предложение по развитию инвестиционного потенциала города Москвы'
    PROPOSAL_SUBTITLE_XPATH = '//*[@id="invest-moscow-app"]/div[10]/p'

    FIRST_DOCUMENT = 'Постановление Правительства Москвы от 13.10.2020 № 1697-ПП «О новом электронном сервисе для сообщений участников инвестиционной деятельности»'
    FIRST_DOCUMENT_XPATH = '//*[@id="invest-moscow-app"]/div[12]/div[1]/a'
    SECOND_DOCUMENT = 'Постановление Правительства Москвы от 22.02.2012 № 66-ПП «О Штабе по защите прав и законных интересов субъектов инвестиционной и предпринимательской деятельности в городе Москве, а также иных рабочих органах Правительства Москвы в сфере инвестиционной и предпринимательской деятельности»'
    SECOND_DOCUMENT_XPATH = '//*[@id="invest-moscow-app"]/div[12]/div[2]/a'




    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title

    def open_mos_investor_page(driver, base_url):
        page = MoscowInvestorPage(driver, base_url)
        page.get()
        return page



