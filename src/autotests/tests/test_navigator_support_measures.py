from autotests.pages.navigator_support_measures_page import NMPPage
import allure
import time

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
        page.get_clicable_by_xpath(page.MEASURES_BUTTON).click()
        nmp = page.get_visible_by_xpath(page.SUPPORT_MEASURES_XPATH)
        nmp.location_once_scrolled_into_view
        assert page.get_clicable_by_xpath(page.FIRST_MEASURE_XPATH).text == page.FIRST_MEASURE
        assert page.get_clicable_by_xpath(page.SECOND_MEASURE_XPATH).text == page.SECOND_MEASURE
        assert page.get_clicable_by_xpath(page.THIRD_MEASURE_XPATH).text == page.THIRD_MEASURE
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")




