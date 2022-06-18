from autotests.pages.PortalPages.main_page import MainPage
import allure


def test_authorization(driver, base_url):
    """Проверка авторизации на портале"""
    with allure.step('1. Открытие главной страницы портала'):
        page = MainPage.open_main_page(driver, base_url)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Открытие окна авторизации'):
        page.login()

    with allure.step('3. Проверка успешной авторизации'):
        page.authorization_check()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")







