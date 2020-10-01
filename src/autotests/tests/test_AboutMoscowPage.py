import pytest
from selenium import webdriver
from autotests.pages.AboutMoscowPage import AboutMoscowPage
from autotests.pages.OnlineServicesPage import OnlineServicesPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def test_check_economics_info(driver):
    '''Проверка переходов по табам и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_info(AboutMoscowPage.ECONOMICS['info'])

def test_check_investments_info(driver):
    '''Проверка переходов по табам и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
    assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])    

def test_check_finance_info(driver):
    '''Проверка переходов по табам и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.FINANCE['tab'])
    assert about_moscow.check_info(AboutMoscowPage.FINANCE['info'])

def test_check_business_info(driver):
    '''Проверка переходов по табам и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.BUSINESS['tab'])
    assert about_moscow.check_info(AboutMoscowPage.BUSINESS['info'])

def test_check_transport_info(driver):
    '''Проверка переходов по табам и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.TRANSPORT['tab'])
    assert about_moscow.check_info(AboutMoscowPage.TRANSPORT['info'])

def test_check_lives_info(driver):
    '''Проверка переходов по табам и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.LIVES['tab'])
    assert about_moscow.check_info(AboutMoscowPage.LIVES['info'])

def test_check_ecology_info(driver):
    '''Проверка переходов по табам и наличие информации'''

    driver.get(AboutMoscowPage.URL)
    about_moscow = AboutMoscowPage(driver)
    assert about_moscow.check_tab(AboutMoscowPage.ECOLOGY['tab'])
    assert about_moscow.check_info(AboutMoscowPage.ECOLOGY['info'])

if __name__ == "__main__":

    pytest.main()