from autotests.pages.DGPMosInvestorPage import DGPMosInvestorPage
import allure
from autotests.pages.DGPMainPage import DGPMainPage
import time

def test_open_page(driver, dgp_base_url):
    """Открытие страницы обращений в мос инвесторе"""
    with allure.step('1. Открыть страницу с обращениями мос инвестора'):
        page = DGPMainPage(driver, dgp_base_url)
        page.get()
        page.login()
        time.sleep(2)
        page = DGPMosInvestorPage(driver, dgp_base_url)
        page.get()
        assert page.get_visible_by_xpath(page.TAB_XPATH).text == page.TAB