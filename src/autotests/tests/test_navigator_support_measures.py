from autotests.pages.navigator_support_measures_page import NMPPage
import allure
import time
from autotests.pages.nmp_calculator_page import NMPCalculator
from selenium.webdriver.support.ui import Select



def test_open_page(driver, base_url):
    """Проверка открытия страницы, нахождения основных элементов и открытия Навигатора мер поддержки"""

    with allure.step('1. Открыть страницу Навигатора мер поддержки'):
        page = NMPPage(driver, base_url)
        page.get()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

    with allure.step('2. Проверить наличие основных элементов'):
        assert page.title == page.TITLE
        assert page.get_visible_by_xpath(page.HEADER_XPATH).text == page.HEADER
        page.get_visible_by_xpath(page.SUBTITLE1_XPATH)
        time.sleep(2)
        assert page.get_visible_by_xpath(page.NUMBER_OF_MEASURES_XPATH).text == page.NUMBER_OF_MEASURES


    with allure.step('3. Проверка загрузки мер поддержки'):
        page.get_clicable_by_xpath(page.MEASURES_BUTTON).location_once_scrolled_into_view
        page.get_clicable_by_xpath(page.MEASURES_BUTTON).click()
        page.get_visible_by_xpath(page.SUPPORT_MEASURES_XPATH).location_once_scrolled_into_view
        assert page.get_clicable_by_xpath(page.FIRST_MEASURE_XPATH).text == page.FIRST_MEASURE
        assert page.get_clicable_by_xpath(page.SECOND_MEASURE_XPATH).text == page.SECOND_MEASURE
        assert page.get_clicable_by_xpath(page.THIRD_MEASURE_XPATH).text == page.THIRD_MEASURE
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")



def test_nmp_calculator(driver, base_url):
    """Проверка работы НМП калькулятора"""
    with allure.step('1. Открыть страницу калькулятора'):
        page = NMPCalculator(driver, base_url)
        page.get()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        assert page.get_visible_by_xpath(page.HEADER_XPATH).text == page.HEADER
        assert page.get_visible_by_xpath(page.SUBTITLE_XPATH).text == page.SUBTITLE
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2.Переход к области калькулятора'):
        page.check_calculator()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step ('3.Расчет данных на калькуляторе'):
        page.check_calculations()
        assert page.get_visible_by_xpath(page.FIRST_CALC_XPATH).text == page.FIRST_CALC
        assert page.get_visible_by_xpath(page.FIRST_CALC_NUMBER_XPATH).text == page.FIRST_CALC_NUMBER
        assert page.get_visible_by_xpath(page.SECOND_CALC_NUMBER_XPATH).text == page.SECOND_CALC_NUMBER
        assert page.get_visible_by_xpath(page.THIRD_CALC_NUMBER_XPATH).text == page.THIRD_CALC_NUMBER
        assert page.get_visible_by_xpath(page.FORTH_CALC_NUMBER_XPATH).text == page.FORTH_CALC_NUMBER
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")



