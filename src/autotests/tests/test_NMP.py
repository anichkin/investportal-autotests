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


def check_nmp_availability(driver):
    driver.get(NMPPage.URL)
    driver.find_element(By.XPATH, '//*[@id="nsmFilters"]/div[2]/h3')


if __name__ == "__main__":

    pytest.main()