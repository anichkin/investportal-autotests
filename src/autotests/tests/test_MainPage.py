import pytest
from selenium import webdriver
from autotests.pages.MainPage import MainPage
from autotests.pages.OnlineServicesPage import OnlineServicesPage


def test_login():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(MainPage.URL)
    main_page = MainPage(driver)
    assert main_page.get_title() == MainPage.TITLE
    main_page.login()
    main_page.get_header_user_name()

def test_go_to_online_services_page():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(MainPage.URL)
    main_page = MainPage(driver)
    main_page.go_to_online_services_page()
    online_services_page = OnlineServicesPage(main_page.driver)
    assert online_services_page.get_title() == OnlineServicesPage.TITLE



if __name__ == "__main__":

    pytest.main()