from autotests.pages.DGPPages.DGPMosInvestorPage import DGPMosInvestorPage
import allure
from autotests.pages.DGPPages.DGPMainPage import DGPMainPage
import time

def test_open_page(driver, dgp_base_url):
    """Открытие страницы обращений в мос инвесторе и открытие первого попавшегося сообщения"""
    with allure.step('1. Авторизация в дгп'):
        page = DGPMainPage(driver, dgp_base_url)
        page.get()
        page.login()
        time.sleep(1)
    with allure.step('2. Открытие раздела Мос инвестора'):
        page = DGPMosInvestorPage(driver, dgp_base_url)
        page.get()
        assert page.get_visible_by_xpath(page.TAB_XPATH).text == page.TAB
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('3. Проверка области сообщений'):
        messages_area = page.get_visible_by_xpath(page.MESSAGES_AREA)
        messages_area.location_once_scrolled_into_view
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('4. Открытие первого сообщения'):
        first_message = page.get_visible_by_xpath(page.FIRST_MESSAGE)
        first_message.click()
        handle = driver.window_handles
        driver.switch_to.window(handle[1])
        common_info = page.get_visible_by_xpath(page.COMMON_INFO_XPATH)
        assert common_info.text == page.COMMON_INFO
        common_info.click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

