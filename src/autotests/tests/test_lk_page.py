from autotests.pages.LKPage import LKPage
from autotests.pages.main_page import MainPage
import allure
import time



def test_main_lk_page(driver, base_url):
    """Открытие главной страницы ЛК и проверка элементов на ней"""

    with allure.step('1. Авторизоваться и открыть главную страницу ЛК'):
        page = MainPage.open_main_page(driver, base_url)
        page.login()
        page.get_header_user_name()
        page = LKPage(driver, base_url)
        page.get()
        assert page.title == page.TITLE

    with allure.step('2. Проверить наличие виджетов Мои Торги'):
        assert page.get_visible_by_xpath(page.MY_TENDERS_XPATH).text == page.MY_TENDERS
        assert page.get_visible_by_xpath(page.MAIN_CONTRACTS_XPATH).text == page.MAIN_CONTRACTS
        assert page.get_visible_by_xpath(page.CONTRACT_INFO_XPATH).text == page.CONTRACT_INFO
        assert page.get_visible_by_xpath(page.MAIN_FAVORITE_TENDERS_XPATH).text == page.MAIN_FAVORITE_TENDERS
        assert page.get_visible_by_xpath(page.ROOM_XPATH).text == page.ROOM
        assert page.get_visible_by_xpath(page.CAR_PLACE_XPATH).text == page.CAR_PLACE
        assert page.get_visible_by_xpath(page.BUILDING_XPATH).text == page.BUILDING
        page.get_visible_by_xpath(page.CALENDAR)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        page.get_visible_by_xpath(page.COMPARE_VIDGET_XPATH).location_once_scrolled_into_view
        assert page.get_visible_by_xpath(page.COMPARE_VIDGET_XPATH).text == page.COMPARE_VIDGET
        assert page.get_visible_by_xpath(page.COMPARE_ROOM_XPATH).text == page.COMPARE_ROOM
        assert page.get_visible_by_xpath(page.COMPARE_CAR_PLACE_XPATH).text == page.COMPARE_CAR_PLACE
        assert page.get_visible_by_xpath(page.COMPARE_NON_CAPITAL_XPATH).text == page.COMPARE_NON_CAPITAL
        assert page.get_visible_by_xpath(page.MY_FILTERS_XPATH).text == page.MY_FILTERS
        assert page.get_visible_by_xpath(page.FILTER_NAME_XPATH).text == page.FILTER_NAME
        page.get_visible_by_xpath(page.FILTER_DATA_XPATH)
        page.get_clicable_by_xpath(page.FILTER_BUTTON)
        page.get_clicable_by_xpath(page.DELETE_FILTER_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        page.get_visible_by_xpath(page.APPLICATION_XPATH).location_once_scrolled_into_view
        assert page.get_visible_by_xpath(page.APPLICATION_XPATH).text == page.APPLICATION
        assert page.get_visible_by_xpath(page.APPLICATION_INFO_XPATH).text == page.APPLICATION_INFO
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

    with allure.step('3. Проверить наличие виджетов блока Мои заявки'):
        page.get_visible_by_xpath(page.MY_APPLICATIONS_XPATH).location_once_scrolled_into_view
        page.get_visible_by_xpath(page.MY_APPLICATIONS_XPATH).text == page.MY_APPLICATIONS
        page.get_visible_by_xpath(page.CITY_TENDERS_XPATH).text == page.CITY_TENDERS
        page.get_visible_by_xpath(page.CITY_TENDERS_INFO_XPATH).text == page.CITY_TENDERS_INFO
        page.get_visible_by_xpath(page.SERVICES_XPATH).text == page.SERVICES
        page.get_visible_by_xpath(page.SERVICES_INFO_XPATH).text == page.SERVICES_INFO
        page.get_visible_by_xpath(page.SUPPORT_MEASURES_XPATH).text == page.SUPPORT_MEASURES
        page.get_visible_by_xpath(page.SUPPORT_MEASURES_INFO_XPATH).text == page.SUPPORT_MEASURES_INFO
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")


def test_my_tenders(driver, base_url):
    with allure.step('1. Открыть вкладку Мои торги'):
        page = LKPage(driver, base_url)
        page.get()
        page.get_clicable_by_xpath(page.MY_TENDERS_TAB).click()
        page.get_visible_by_xpath(page.APPLICATION_TAB)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        page.logout_from_lk(driver,base_url)









