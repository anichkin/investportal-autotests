import pytest
from selenium import webdriver
from autotests.pages.MainPage import MainPage


def test_MainPage():

    driver = webdriver.Chrome()
    driver.get(MainPage.URL)
    main_page = MainPage(driver)
    assert main_page.get_title() == 'Главная - Инвестиционный портал Москвы'
    login_input, password_input = main_page.press_to_login_pic()
    login_input.send_keys(MainPage.LOGIN)
    password_input.send_keys(MainPage.PASSWORD)


if __name__ == "__main__":

    pytest.main()