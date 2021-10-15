from autotests.pages.about_moscow_page import AboutMoscowPage
from autotests.pages.moscow_in_numbers_page import MoscowInNumberPage
from autotests.pages.podpiska_inwest_digest_page import PodpiskaInwestDigestPage
from autotests.pages.investment_map_page import InvestmentMapPage
from autotests.pages.projects_page import ProjectsPage


def test_check_economics_info(driver, base_url):
    '''Проверка перехода в "Экономика" и наличие информации'''

    about_moscow = AboutMoscowPage(driver, base_url)
    print(about_moscow.url)
    about_moscow.get()
    assert about_moscow.check_info(AboutMoscowPage.ECONOMICS['info'])

# def test_check_investments_info(driver, base_url):
#     '''Проверка перехода в "Инвестиции" и наличие информации'''


#     assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
#     assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])    

def test_check_finance_info(driver, base_url):
    '''Проверка перехода в "Финансы" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.FINANCE['tab'])
    assert about_moscow.check_info(AboutMoscowPage.FINANCE['info'])

def test_check_business_info(driver, base_url):
    '''Проверка перехода в "Условия для бизнеса" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.BUSINESS['tab'])
    assert about_moscow.check_info(AboutMoscowPage.BUSINESS['info'])

def test_check_transport_info(driver, base_url):
    '''Проверка перехода в "Транспорт" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.TRANSPORT['tab'])
    assert about_moscow.check_info(AboutMoscowPage.TRANSPORT['info'])

def test_check_lives_info(driver, base_url):
    '''Проверка перехода в "Качество жизни" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.LIVES['tab'])
    assert about_moscow.check_info(AboutMoscowPage.LIVES['info'])

def test_check_ecology_info(driver, base_url):
    '''Проверка перехода в "Экология" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.ECOLOGY['tab'])
    assert about_moscow.check_info(AboutMoscowPage.ECOLOGY['info'])


def test_check_details(driver, base_url):
    '''Проверям переход по кнопке Подробнее и нажатие на динамеческое меню'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    moscow_in_number = MoscowInNumberPage(driver)
    about_moscow.check_details()
    assert moscow_in_number.get_title() == MoscowInNumberPage.TITLE
    moscow_in_number.check_blocks_and_menu()
    moscow_in_number.check_brochure()


def test_check_podpiska(driver, base_url):
    '''Проверяем подписку'''

    driver.get(MoscowInNumberPage.URL)
    moscow_in_number = MoscowInNumberPage(driver)
    moscow_in_number.check_podpiska()
    driver.get(PodpiskaInwestDigestPage.URL)
    podpiska_inwest_digest = PodpiskaInwestDigestPage(driver)
    assert podpiska_inwest_digest.get_title() == PodpiskaInwestDigestPage.TITLE



def test_check_brochure(driver, base_url):
    '''Проверяем кнопку Скачать брошюру'''

    driver.get(MoscowInNumberPage.URL)
    moscow_in_number = MoscowInNumberPage(driver)
    moscow_in_number.check_brochure()
    
    
def test_check_map(driver, base_url):
    '''Проверка показа инвесткарты'''

    driver.get(InvestmentMapPage.URL)
    investment_map = InvestmentMapPage(driver)
    investment_map.check_map()


def test_check_projects(driver, base_url):

    driver.get(ProjectsPage.URL)
    projects = ProjectsPage(driver)
    assert projects.get_title() == 'Проекты - Инвестиционный портал Москвы'
    projects.check_projects()
