import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.MainPage import MainPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def is_loaded(driver):
    return driver.execute_script('return document.readyState;')
        


def test_time(driver):
    driver.get(MainPage.URL)
    print(WebDriverWait(driver, 10).until(is_loaded))



