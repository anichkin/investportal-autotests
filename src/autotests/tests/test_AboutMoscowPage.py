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

# def test_check_economics_info(driver):
#     '''Проверка переходов по табам и наличие информации'''

#     driver.get(AboutMoscowPage.URL)
#     about_moscow = AboutMoscowPage(driver)
#     assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
#     assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])

# def test_check_economics_info(driver):
#     '''Проверка переходов по табам и наличие информации'''

#     driver.get(AboutMoscowPage.URL)
#     about_moscow = AboutMoscowPage(driver)
#     assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
#     assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])

# def test_check_economics_info(driver):
#     '''Проверка переходов по табам и наличие информации'''

#     driver.get(AboutMoscowPage.URL)
#     about_moscow = AboutMoscowPage(driver)
#     assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
#     assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])

# def test_check_economics_info(driver):
#     '''Проверка переходов по табам и наличие информации'''

#     driver.get(AboutMoscowPage.URL)
#     about_moscow = AboutMoscowPage(driver)
#     assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
#     assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])

# def test_check_economics_info(driver):
#     '''Проверка переходов по табам и наличие информации'''

#     driver.get(AboutMoscowPage.URL)
#     about_moscow = AboutMoscowPage(driver)
#     assert about_moscow.check_tab(AboutMoscowPage.INVESTMENTS['tab'])
#     assert about_moscow.check_info(AboutMoscowPage.INVESTMENTS['info'])

if __name__ == "__main__":

    pytest.main()