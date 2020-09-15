import pytest
from selenium import webdriver
from autotests.pages.MainLoginPage import MainLoginPage


def test_MainLoginPage():

    driver = webdriver.Chrome()
    driver.get(MainLoginPage.URL)
    main_page = MainLoginPage(driver)
    assert main_page.get_title() == 'Главная - Инвестиционный портал Москвы'
    login_input, password_input = main_page.press_to_login_pic()
    login_input.send_keys(MainLoginPage.LOGIN)
    password_input.send_keys(MainLoginPage.PASSWORD)


if __name__ == "__main__":

    pytest.main()