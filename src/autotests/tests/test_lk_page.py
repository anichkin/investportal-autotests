from autotests.pages.PortalPages.LKPages.LKMainPage import LKPage
from autotests.pages.PortalPages.main_page import MainPage
from autotests.pages.PortalPages.LKPages.MyTenderPage import MyTenderPage
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
        my_tenders = main_lk.get_visible_by_css_long(main_lk.MY_TENDERS_SELECTOR)
        assert my_tenders.text == main_lk.MY_TENDERS
        assert main_lk.get_visible_by_css(main_lk.MAIN_CONTRACTS_SELECTOR).text == main_lk.MAIN_CONTRACTS
        assert main_lk.get_visible_by_css(main_lk.CONTRACT_INFO_SELECTOR).text == main_lk.CONTRACT_INFO
        assert main_lk.get_visible_by_css(main_lk.MAIN_FAVORITE_TENDERS_SELECTOR).text == main_lk.MAIN_FAVORITE_TENDERS
        assert main_lk.get_visible_by_xpath(main_lk.ROOM_XPATH).text == main_lk.ROOM
        assert main_lk.get_visible_by_xpath(main_lk.CAR_PLACE_XPATH).text == main_lk.CAR_PLACE
        assert main_lk.get_visible_by_xpath(main_lk.BUILDING_XPATH).text == main_lk.BUILDING
        main_lk.get_visible_by_xpath(main_lk.CALENDAR)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        compare_vidget = main_lk.get_visible_by_xpath(main_lk.COMPARE_VIDGET_XPATH)
        compare_vidget.location_once_scrolled_into_view
        assert compare_vidget.text == main_lk.COMPARE_VIDGET
        assert main_lk.get_visible_by_xpath(main_lk.COMPARE_ROOM_XPATH).text == main_lk.COMPARE_ROOM
        assert main_lk.get_visible_by_xpath(main_lk.COMPARE_CAR_PLACE_XPATH).text == main_lk.COMPARE_CAR_PLACE
        assert main_lk.get_visible_by_xpath(main_lk.COMPARE_NON_CAPITAL_XPATH).text == main_lk.COMPARE_NON_CAPITAL
        assert main_lk.get_visible_by_xpath(main_lk.MY_FILTERS_XPATH).text == main_lk.MY_FILTERS
        assert main_lk.get_visible_by_xpath(main_lk.FILTER_NAME_XPATH).text == main_lk.FILTER_NAME
        main_lk.get_visible_by_xpath(main_lk.FILTER_DATA_XPATH)
        main_lk.get_clicable_by_xpath(main_lk.FILTER_BUTTON)
        main_lk.get_clicable_by_xpath(main_lk.DELETE_FILTER_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        applications = main_lk.get_visible_by_xpath(main_lk.APPLICATION_XPATH)
        applications.location_once_scrolled_into_view
        assert applications.text == main_lk.APPLICATION
        assert main_lk.get_visible_by_xpath(main_lk.APPLICATION_INFO_XPATH).text == main_lk.APPLICATION_INFO
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

    with allure.step('3. Проверить наличие виджетов блока Мои заявки'):
        my_applications = main_lk.get_visible_by_xpath(main_lk.MY_APPLICATIONS_XPATH)
        my_applications.location_once_scrolled_into_view
        my_applications.text == main_lk.MY_APPLICATIONS
        assert main_lk.get_visible_by_xpath(main_lk.CITY_TENDERS_XPATH).text == main_lk.CITY_TENDERS
        assert main_lk.get_visible_by_xpath(main_lk.CITY_TENDERS_INFO_XPATH).text == main_lk.CITY_TENDERS_INFO
        assert main_lk.get_visible_by_xpath(main_lk.SERVICES_XPATH).text == main_lk.SERVICES
        assert main_lk.get_visible_by_xpath(main_lk.SERVICES_INFO_XPATH).text == main_lk.SERVICES_INFO
        assert main_lk.get_visible_by_xpath(main_lk.SUPPORT_MEASURES_XPATH).text == main_lk.SUPPORT_MEASURES
        assert main_lk.get_visible_by_xpath(main_lk.SUPPORT_MEASURES_INFO_XPATH).text == main_lk.SUPPORT_MEASURES_INFO
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")


def test_my_tenders(driver, base_url):
    """Открытие вкладки Мои Торги в личном кабинете
        Открыть вкладку договоры: проверить количество договоров
        Открыть вкладку Избранные торги, проверить наличие первых избранных торгов и их общее количество
        Открыть вкладу Мои фильтры, проверить наличие первого фильтра и общее количество
        Открыть вкладку сравнение торгов: проверить наличие первых торгов и их общее количество
        """
    with allure.step('1. Авторизоваться и открыть главную страницу ЛК'):
        main_lk = MainPage.open_main_page(driver, base_url)
        main_lk.login()
        main_lk.authorization_check()

    with allure.step('2. Открыть вкладку Мои торги - Заявки'):
        page = MyTenderPage(driver, base_url)
        page.get()
        assert page.get_visible_by_xpath_long(page.APPLICATION_TAB_XPATH).text == page.APPLICATION_TAB
        contract_tab = page.get_visible_by_xpath_long(page.CONTRACT_TAB_XPATH)
        assert contract_tab.text == page.CONTRACT_TAB
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('3. Открыть вкладку Договоры, проверить количество'):
        contract_tab.click()
        contract_amount = page.get_visible_by_xpath_long(page.AMOUNT_CHECK)
        assert contract_amount.text == page.CONTRACT_AMOUNT
        favorite_tab = page.get_visible_by_xpath(page.FAVORITE_XPATH)
        assert favorite_tab.text == page.FAVORITE
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('4. Открыть вкладку Избранные торги, проверить первые торги и количество'):
        favorite_tab.click()
        page.get_visible_by_css(page.FIRST_FAVORITE_TENDER)
        tender_name = page.get_visible_by_xpath_long(page.TENDER_NAME_XPATH)
        assert tender_name.text == page.TENDER_NAME
        favorite_amount = page.get_visible_by_xpath_long(page.AMOUNT_CHECK)
        assert favorite_amount.text == page.FAVORITE_AMOUNT
        my_filters_tab = page.get_visible_by_xpath(page.MY_FILTERS_TAB_XPATH)
        assert my_filters_tab.text == page.MY_FILTERS_TAB
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('5. Открыть вкладку Мои фильтры, проверить первый фильтр и количество'):
        my_filters_tab.click()
        page.get_visible_by_xpath_long(page.FIRST_FILTER)
        filter_name = page.get_visible_by_xpath_long(page.FIRST_FILTER_NAME_XPATH)
        assert filter_name.text == page.FIRST_FILTER_NAME
        filters_amount = page.get_visible_by_xpath_long(page.AMOUNT_CHECK)
        assert filters_amount.text == page.FILTERS_AMOUNT
        compare_tab = page.get_visible_by_xpath(page.COMPARE_TAB_XPATH)
        assert compare_tab.text == page.COMPARE_TAB
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('6. Открыть вкладку Сравнение объектов, проверить первый объект и количество'):
        compare_tab.click()
        page.get_visible_by_xpath_long(page.COMPARE_AREA)
        first_tender_name = page.get_visible_by_xpath_long(page.FIRST_TENDER_NAME_XPATH)
        assert first_tender_name.text == page.FIRST_TENDER_NAME
        compare_amount = page.get_visible_by_xpath_long(page.AMOUNT_CHECK)
        assert compare_amount.text == page.COMPARE_AMOUNT
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")




















