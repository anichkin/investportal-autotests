from autotests.pages.NewInvestMapPage import NewInvestMapPage
import allure

def test_open_map(driver, base_url):
    with allure.step('1. Открыть страницу с картой'):
        page = NewInvestMapPage(driver, base_url)
        page.get()
    with allure.step('2. Проверить наличие подложки карты и сайдбара'):
        assert page.title == page.TITLE
        page.get_visible_by_xpath(page.INVESTMAP_AREA)
        page.get_visible_by_xpath(page.SIDEBAR_AREA)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

