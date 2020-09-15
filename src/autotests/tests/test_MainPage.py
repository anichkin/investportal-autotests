import pytest
from selenium import webdriver
from autotests.pages.MainPage import MainPage


def test_MainPage():

    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    assert main_page.get_title() == 'Главная - Инвестиционный портал Москвы'
    main_page.press_to_login_pic()


if __name__ == "__main__":

    pytest.main()