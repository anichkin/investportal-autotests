from autotests.pages.main_page import MainPage
import allure
from autotests.pages.LogoutPage import LogoutPage
from autotests.pages.LKPage import LKPage




def test_authorization(driver, base_url):
    with allure.step('1. Открытие главной страницы портала'):
        page = MainPage.open_main_page(driver, base_url)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Открытие окна авторизации'):
        page.login()

    with allure.step('3. Проверка успешной авторизации'):
        page.authorization_check()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")







