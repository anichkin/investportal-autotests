import time

import pytest
from selenium import webdriver
from autotests.pages.MainPage import MainPage
from autotests.pages.NMPPage import NMPPage
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def test_nmp_availability(driver):
    driver.get(NMPPage.URL)
    nmp_page = NMPPage(driver)
    time.sleep(5)
    nmp_page.check_elements()
    time.sleep(10)


if __name__ == "__main__":

    pytest.main()