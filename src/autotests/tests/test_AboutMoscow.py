import pytest
from selenium import webdriver
from autotests.pages.AboutMoscowPage import AboutMoscowPage
from autotests.pages.MoscowInNumbersPage import MoscowInNumberPage
from autotests.pages.PodpiskaInwestDigestPage import PodpiskaInwestDigestPage
from autotests.pages.InvestmentMapPage import InvestmentMapPage
from autotests.pages.ProjectsPage import ProjectsPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def test_check_economics_info(driver):
    '''Проверка перехода в "Экономика" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_info(AboutMoscowPage.ECONOMICS['info'])

def test_check_investments_info(driver):
    '''Проверка перехода в "Инвестиции" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
    assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])    

def test_check_finance_info(driver):
    '''Проверка перехода в "Финансы" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.FINANCE['tab'])
    assert about_moscow.check_info(AboutMoscowPage.FINANCE['info'])

def test_check_business_info(driver):
    '''Проверка перехода в "Условия для бизнеса" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.BUSINESS['tab'])
    assert about_moscow.check_info(AboutMoscowPage.BUSINESS['info'])

def test_check_transport_info(driver):
    '''Проверка перехода в "Транспорт" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.TRANSPORT['tab'])
    assert about_moscow.check_info(AboutMoscowPage.TRANSPORT['info'])

def test_check_lives_info(driver):
    '''Проверка перехода в "Качество жизни" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.LIVES['tab'])
    assert about_moscow.check_info(AboutMoscowPage.LIVES['info'])

def test_check_ecology_info(driver):
    '''Проверка перехода в "Экология" и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.ECOLOGY['tab'])
    assert about_moscow.check_info(AboutMoscowPage.ECOLOGY['info'])


def test_check_details(driver):
    '''Проверям переход по кнопке Подробнее и нажатие на динамеческое меню'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    moscow_in_number = MoscowInNumberPage(driver)
    about_moscow.check_details()
    assert moscow_in_number.get_title() == 'Москва в цифрах - Инвестиционный портал Москвы'
    # moscow_in_number.check_blocks_and_menu()
    moscow_in_number.check_brochure()


def test_check_podpiska(driver):
    '''Проверяем подписку'''

    driver.get(MoscowInNumberPage.URL)
    moscow_in_number = MoscowInNumberPage(driver)
    moscow_in_number.check_podpiska()
    driver.get(PodpiskaInwestDigestPage.URL)
    podpiska_inwest_digest = PodpiskaInwestDigestPage(driver)
    assert podpiska_inwest_digest.get_title() == PodpiskaInwestDigestPage.TITLE



def test_check_brochure(driver):
    '''Проверяем кнопку Скачать брошюру'''

    driver.get(MoscowInNumberPage.URL)
    moscow_in_number = MoscowInNumberPage(driver)
    moscow_in_number.check_brochure()
    

def test_check_map(driver):
    '''Проверка показа инвесткарты'''

    driver.get(InvestmentMapPage.URL)
    investment_map = InvestmentMapPage(driver)
    investment_map.check_map()


def test_check_projects(driver):

    driver.get(ProjectsPage.URL)
    projects = ProjectsPage(driver)
    assert projects.get_title() == 'Проекты - Инвестиционный портал Москвы'
    projects.check_projects()



if __name__ == "__main__":

    pytest.main()