import time
import pytest
from selenium import webdriver
from autotests.pages.NMPPage import NMPPage
from autotests.pages.NMPCalculatorPage import NMPCalculator
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def test_nmp_availability(driver):
    driver.get(NMPPage.URL)
    nmp_page = NMPPage(driver)
    nmp_page.check_filters()
    nmp_page.check_measures()
    nmp_page.check_export()


def test_nmp_calculator(driver):
    driver.get(NMPCalculator.URL)
    nmp_calculator = NMPCalculator(driver)
    nmp_calculator.check_calculator()

if __name__ == "__main__":

    pytest.main()