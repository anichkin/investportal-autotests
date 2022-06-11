from autotests.pages.LKPage import LKPage
from autotests.pages.main_page import MainPage
import allure
import time



def test_main_lk_page(driver, base_url):
    """Открытие главной страницы ЛК и проверка элементов на ней"""

    with allure.step('1. Авторизоваться и открыть главную страницу ЛК'):
        main_lk = MainPage.open_main_page(driver, base_url)
        main_lk.login()
        main_lk.authorization_check()
        main_lk = LKPage(driver, base_url)
        main_lk.get()
        assert main_lk.title == main_lk.TITLE

    with allure.step('2. Проверить наличие виджетов Мои Торги'):
        assert main_lk.get_visible_by_xpath(main_lk.MY_TENDERS_XPATH).text == main_lk.MY_TENDERS
        assert main_lk.get_visible_by_xpath(main_lk.MAIN_CONTRACTS_XPATH).text == main_lk.MAIN_CONTRACTS
        assert main_lk.get_visible_by_xpath(main_lk.CONTRACT_INFO_XPATH).text == main_lk.CONTRACT_INFO
        assert main_lk.get_visible_by_xpath(main_lk.MAIN_FAVORITE_TENDERS_XPATH).text == main_lk.MAIN_FAVORITE_TENDERS
        assert main_lk.get_visible_by_xpath(main_lk.ROOM_XPATH).text == main_lk.ROOM
        assert main_lk.get_visible_by_xpath(main_lk.CAR_PLACE_XPATH).text == main_lk.CAR_PLACE
        assert main_lk.get_visible_by_xpath(main_lk.BUILDING_XPATH).text == main_lk.BUILDING
        main_lk.get_visible_by_xpath(main_lk.CALENDAR)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        main_lk.get_visible_by_xpath(main_lk.COMPARE_VIDGET_XPATH).location_once_scrolled_into_view
        assert main_lk.get_visible_by_xpath(main_lk.COMPARE_VIDGET_XPATH).text == main_lk.COMPARE_VIDGET
        assert main_lk.get_visible_by_xpath(main_lk.COMPARE_ROOM_XPATH).text == main_lk.COMPARE_ROOM
        assert main_lk.get_visible_by_xpath(main_lk.COMPARE_CAR_PLACE_XPATH).text == main_lk.COMPARE_CAR_PLACE
        assert main_lk.get_visible_by_xpath(main_lk.COMPARE_NON_CAPITAL_XPATH).text == main_lk.COMPARE_NON_CAPITAL
        assert main_lk.get_visible_by_xpath(main_lk.MY_FILTERS_XPATH).text == main_lk.MY_FILTERS
        assert main_lk.get_visible_by_xpath(main_lk.FILTER_NAME_XPATH).text == main_lk.FILTER_NAME
        main_lk.get_visible_by_xpath(main_lk.FILTER_DATA_XPATH)
        main_lk.get_clicable_by_xpath(main_lk.FILTER_BUTTON)
        main_lk.get_clicable_by_xpath(main_lk.DELETE_FILTER_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        main_lk.get_visible_by_xpath(main_lk.APPLICATION_XPATH).location_once_scrolled_into_view
        assert main_lk.get_visible_by_xpath(main_lk.APPLICATION_XPATH).text == main_lk.APPLICATION
        assert main_lk.get_visible_by_xpath(main_lk.APPLICATION_INFO_XPATH).text == main_lk.APPLICATION_INFO
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

    with allure.step('3. Проверить наличие виджетов блока Мои заявки'):
        main_lk.get_visible_by_xpath(main_lk.MY_APPLICATIONS_XPATH).location_once_scrolled_into_view
        main_lk.get_visible_by_xpath(main_lk.MY_APPLICATIONS_XPATH).text == main_lk.MY_APPLICATIONS
        main_lk.get_visible_by_xpath(main_lk.CITY_TENDERS_XPATH).text == main_lk.CITY_TENDERS
        main_lk.get_visible_by_xpath(main_lk.CITY_TENDERS_INFO_XPATH).text == main_lk.CITY_TENDERS_INFO
        main_lk.get_visible_by_xpath(main_lk.SERVICES_XPATH).text == main_lk.SERVICES
        main_lk.get_visible_by_xpath(main_lk.SERVICES_INFO_XPATH).text == main_lk.SERVICES_INFO
        main_lk.get_visible_by_xpath(main_lk.SUPPORT_MEASURES_XPATH).text == main_lk.SUPPORT_MEASURES
        main_lk.get_visible_by_xpath(main_lk.SUPPORT_MEASURES_INFO_XPATH).text == main_lk.SUPPORT_MEASURES_INFO
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")


def test_my_tenders(driver, base_url):
    with allure.step('1. Авторизоваться и открыть главную страницу ЛК'):
        main_lk = MainPage.open_main_page(driver, base_url)
        main_lk.login()
        main_lk.authorization_check()

    with allure.step('2. Открыть вкладку Мои торги'):
        tender_tab_page = LKPage(driver, base_url)
        tender_tab_page.get()
        tender_tab_page.get_clicable_by_xpath(tender_tab_page.MY_TENDERS_TAB).click()
        tender_tab_page.get_visible_by_xpath(tender_tab_page.APPLICATION_TAB)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")










