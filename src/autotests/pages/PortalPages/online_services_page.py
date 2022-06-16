from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage


class OnlineServicesPage(BasePage):

    PATH = '/online-services'
    TITLE = 'Онлайн-сервисы - Инвестиционный портал Москвы'
    HEADER_XPATH = '//*[@id="uid-portal"]/div/div[1]/div/h1'
    HEADER = 'ОНЛАЙН-СЕРВИСЫ'
    SUBTITLE_XPATH = '//*[@id="uid-portal"]/div/div[1]/div/p'
    SUBTITLE = 'Онлайн-сервисы Инвестиционного портала – это набор электронных сервисов для упрощения и сокращения сроков процессов взаимодействия с органами исполнительной власти и подведомственными организациями Правительства Москвы'
    SCROLL_BAR = '//*[@id="uid-portal"]/div/div[1]/div/aside'
    DIRECT_CONNECTION = '.scroll-bar__buttons > div:nth-child(1) > button'
    DIRECT_CONNECTION_HEADER = 'ПРЯМАЯ СВЯЗЬ'
    DIRECT_CONNECTION_HEADER_XPATH = '//*[@id="Communication"]/div[1]/h2'
    DIRECT_CONNECTION_FULL_LIST = '//*[@id="Communication"]/div[1]/div/button'
    DIRECT_CONNECTION_SUBTITLE_XPATH = '//*[@id="Communication"]/div[1]/p'
    DIRECT_CONNECTION_SUBTITLE = 'Официальный канал Правительства Москвы, созданный для оперативного решения вопросов, возникающих в процессе инвестиционной и предпринимательской деятельности в городе, а также участия в городских торгах'
    DIRECT_CONNECTION_HEADER2_XPATH = '//*[@id="Communication"]/div[1]/div/div[1]/h4'
    DIRECT_CONNECTION_HEADER2 = 'СПИСОК КАНАЛОВ ПРЯМОЙ СВЯЗИ, ПРЕДСТАВЛЕННЫХ НА ПОРТАЛЕ 4'
    LPO_BLOCK_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[1]/div[2]/h3'
    LPO_BLOCK = 'ЛИНИЯ ПРЯМЫХ ОБРАЩЕНИЙ'
    LPO_SUBTITLE_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[1]/div[2]/p[2]'
    LPO_SUBTITLE = 'Задать вопрос и получить консультацию'
    LPO_BUTTON_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[1]/a'
    LPO_BUTTON = 'Написать'
    MOS_INVESTOR_HEADER_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[2]/div[2]/h3'
    MOS_INVESTOR_HEADER = 'МОСКОВСКИЙ ИНВЕСТОР'
    MOS_INVESTOR_SUBTITLE_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[2]/div[2]/p[2]'
    MOS_INVESTOR_SUBTITLE = 'Оперативное рассмотрение проблем и предложений инвесторов'
    MOS_INVESTOR_BUTTON_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[2]/a'
    MOS_INVESTOR_BUTTON = 'Перейти'
    COVID_HEADER_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[3]/div[2]/h3'
    COVID_HEADER = 'STOP-COVID19'
    COVID_SUBTITLE_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[3]/div[2]/p[2]'
    COVID_SUBTITLE = 'Отвечаем на важные вопросы по ведению бизнеса в Москве в условиях эпидемии коронавируса'
    COVID_BUTTON_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[3]/a'
    COVID_BUTTON = 'Перейти'
    INFORM_KIOSK_HEADER_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[4]/div[2]/h3'
    INFORM_KIOSK_HEADER = 'ОБРАТИТЬСЯ В «ИНФОРМАЦИОННЫЙ КИОСК»'
    INFORM_KIOSK_SUBTITLE_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[4]/div[2]/p[2]'
    INFORM_KIOSK_SUBTITLE = 'Задать вопрос по торгам'
    INFORM_KIOSK_BUTTON_XPATH = '//*[@id="Communication"]/div[1]/div/div[2]/a[4]/a'
    INFORM_KIOSK_BUTTON = 'Подробнее'
    SERVICES = '.scroll-bar__buttons > div:nth-child(2) > button'
    SERVICES_HEADER_XPATH = '//*[@id="Services"]/div[1]/h2'
    SERVICES_HEADER = 'УСЛУГИ'
    SERVICES_SUBTITLE_XPATH = '//*[@id="Services"]/div[1]/p'
    SERVICES_SUBTITLE = 'Сервисы для инвесторов и предпринимателей, планирующих реализовать свой проект на территории города. Подача инвестиционных инициатив и заявок на подбор площадки для локализации в режиме онлайн'
    SERVICES_FULL_LIST = '//*[@id="Services"]/div[1]/div/button'
    SERVICES_HEADER2_XPATH = '//*[@id="Services"]/div[1]/div/div[1]/h4'
    SERVICES_HEADER2 = 'СПИСОК УСЛУГ, ЗАЯВКИ НА КОТОРЫЕ МОЖНО ПОДАТЬ ОНЛАЙН 6'
    INVEST_PROJECT_HEADER_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[1]/div[2]/h3'
    INVEST_PROJECT_HEADER = 'НАПРАВИТЬ ИНВЕСТИЦИОННЫЙ ПРОЕКТ'
    INVEST_PROJECT_SUBTITLE_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[1]/div[2]/p[2]'
    INVEST_PROJECT_SUBTITLE = 'Изучим Ваш проект. Предложим меры поддержки. Окажем содействие в реализации'
    INVEST_PROJECT_BUTTON_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[1]/a'
    INVEST_PROJECT_BUTTON = 'Направить'
    RENT_ROOM_HEADER_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[2]/div[2]/h3'
    RENT_ROOM_HEADER = 'АРЕНДА ПОМЕЩЕНИЙ В ТЕХНОПАРКАХ'
    RENT_ROOM_SUBTITLE_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[2]/div[2]/p[2]'
    RENT_ROOM_SUBTITLE = 'Направить онлайн заявку на аренду свободных помещений'
    RENT_ROOM_BUTTON_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[2]/a'
    RENT_ROOM_BUTTON = 'Направить'
    REQUEST_FOR_AREA_HEADER_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[3]/div[2]/h3'
    REQUEST_FOR_AREA_HEADER = 'ЗАЯВКА НА ПОДБОР ПРОМЫШЛЕННОЙ ПЛОЩАДКИ'
    REQUEST_FOR_AREA_SUBTITLE_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[3]/div[2]/p[2]'
    REQUEST_FOR_AREA_SUBTITLE = 'Подберем варианты размещения Вашего производства на территории города'
    REQUEST_FOR_AREA_BUTTON_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[3]/a'
    REQUEST_FOR_AREA_BUTTON = 'Направить'
    INCLUDING_IN_REESTR_HEADER_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[4]/div[2]/h3'
    INCLUDING_IN_REESTR_HEADER = 'ВКЛЮЧЕНИЕ В РЕЕСТР ПРОМПЛОЩАДОК'
    INCLUDING_IN_REESTR_SUBTITLE_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[4]/div[2]/p[2]'
    INCLUDING_IN_REESTR_SUBTITLE = 'Заявка на включение в реестр промышленных площадок'
    INCLUDING_IN_REESTR_BUTTON_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[4]/a'
    INCLUDING_IN_REESTR_BUTTON = 'Подать заявку'
    CONCESSION_INITIATIVE_HEADER_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[5]/div[2]/h3'
    CONCESSION_INITIATIVE_HEADER = 'НАПРАВИТЬ КОНЦЕССИОННУЮ ИНИЦИАТИВУ'
    CONCESSION_INITIATIVE_SUBTITLE_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[5]/div[2]/p[2]'
    CONCESSION_INITIATIVE_SUBTITLE = 'Проработаем и предложим варианты реализации проекта'
    CONCESSION_INITIATIVE_BUTTON_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[5]/a'
    CONCESSION_INITIATIVE_BUTTON = 'Направить'
    INVEST_CATALOG_HEADER_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[6]/div[2]/h3'
    INVEST_CATALOG_HEADER = 'ИНВЕСТИЦИОННЫЙ КАТАЛОГ'
    INVEST_CATALOG_SUBTITLE_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[6]/div[2]/p[2]'
    INVEST_CATALOG_SUBTITLE = 'Экспозиция неиспользуемого городского имущества, которое может быть выставлено на торги'
    INVEST_CATALOG_BUTTON_XPATH = '//*[@id="Services"]/div[1]/div/div[2]/a[6]/a'
    INVEST_CATALOG_BUTTON = 'Перейти'

    block = ''


    def get_title(self):

        return self.driver.title


    def open_online_services_page(driver, base_url, block):
        page = OnlineServicesPage(driver, base_url)
        page.get()
        try:
            page.get_clicable_by_css(block).click()
        except Exception:
            return page
        return page

