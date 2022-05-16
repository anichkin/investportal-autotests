from autotests.pages.about_moscow_page import AboutMoscowPage
from autotests.pages.moscow_in_numbers_page import MoscowInNumberPage
from autotests.pages.podpiska_inwest_digest_page import PodpiskaInwestDigestPage
from autotests.pages.investment_map_page import InvestmentMapPage
from autotests.pages.projects_page import ProjectsPage


def test_check_economics_info(driver, base_url):
    '''Проверка перехода в "Экономика" и наличие информации'''
    about_moscow = AboutMoscowPage(driver, base_url)
    about_moscow.get()
    assert about_moscow.check_info(AboutMoscowPage.ECONOMICS['info'])

# def test_check_investments_info(driver, base_url):
#     '''Проверка перехода в "Инвестиции" и наличие информации'''


#     assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
#     assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])    

def test_check_finance_info(driver, base_url):
    '''Проверка перехода в "Финансы" и наличие информации'''

    about_moscow = AboutMoscowPage(driver, base_url)
    about_moscow.get()
    assert about_moscow.check_tab(AboutMoscowPage.FINANCE['tab'])
    assert about_moscow.check_info(AboutMoscowPage.FINANCE['info'])

def test_check_business_info(driver, base_url):
    '''Проверка перехода в "Условия для бизнеса" и наличие информации'''
    about_moscow = AboutMoscowPage(driver, base_url)
    about_moscow.get()
    assert about_moscow.check_tab(AboutMoscowPage.BUSINESS['tab'])
    assert about_moscow.check_info(AboutMoscowPage.BUSINESS['info'])

def test_check_transport_info(driver, base_url):
    '''Проверка перехода в "Транспорт" и наличие информации'''

    about_moscow = AboutMoscowPage(driver, base_url)
    about_moscow.get()
    assert about_moscow.check_tab(AboutMoscowPage.TRANSPORT['tab'])
    assert about_moscow.check_info(AboutMoscowPage.TRANSPORT['info'])

def test_check_lives_info(driver, base_url):
    '''Проверка перехода в "Качество жизни" и наличие информации'''

    about_moscow = AboutMoscowPage(driver, base_url)
    about_moscow.get()
    assert about_moscow.check_tab(AboutMoscowPage.LIVES['tab'])
    assert about_moscow.check_info(AboutMoscowPage.LIVES['info'])

def test_check_ecology_info(driver, base_url):
    '''Проверка перехода в "Экология" и наличие информации'''

    about_moscow = AboutMoscowPage(driver, base_url)
    about_moscow.get()
    assert about_moscow.check_tab(AboutMoscowPage.ECOLOGY['tab'])
    assert about_moscow.check_info(AboutMoscowPage.ECOLOGY['info'])


def test_check_details(driver, base_url):
    '''Проверям переход по кнопке Подробнее и нажатие на динамеческое меню'''

    about_moscow = AboutMoscowPage(driver, base_url)
    about_moscow.get()
    about_moscow.check_details()
    moscow_in_number = MoscowInNumberPage(driver, base_url)
    moscow_in_number.get()
    assert moscow_in_number.get_title() == MoscowInNumberPage.TITLE
    moscow_in_number.check_blocks_and_menu()
    moscow_in_number.check_brochure()


# def test_check_podpiska(driver, base_url):
#     '''Проверяем подписку'''
#
#     moscow_in_number = MoscowInNumberPage(driver, base_url)
#     moscow_in_number.get()
#     moscow_in_number.check_podpiska()
#     podpiska_inwest_digest = PodpiskaInwestDigestPage(driver,base_url)
#     podpiska_inwest_digest.get()
#     assert podpiska_inwest_digest.get_title() == PodpiskaInwestDigestPage.TITLE


# исправить
# def test_check_brochure(driver, base_url):
#     '''Проверяем кнопку Скачать брошюру'''

#     moscow_in_number = MoscowInNumberPage(driver, base_url)
#     moscow_in_number.get()
#     moscow_in_number.check_brochure()
    
# исправить   
# def test_check_map(driver, base_url):
#     '''Проверка показа инвесткарты'''

#     investment_map = InvestmentMapPage(driver,base_url)
#     investment_map.get()
#     investment_map.check_map()

# исправить
# def test_check_projects(driver, base_url):

#     projects = ProjectsPage(driver,base_url)
#     projects.get()
#     assert projects.get_title() == 'Проекты - Инвестиционный портал Москвы'
#     projects.check_projects()
