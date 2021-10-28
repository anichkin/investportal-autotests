import pytest
from selenium import webdriver
from autotests.pages.IndustriesPage import IndustriesPage
from selenium.webdriver.common.by import By



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def test_blocks(driver):
    driver.get(IndustriesPage.URL)
    industries = IndustriesPage(driver)
    industries.check_blocks()





if __name__ == "__main__":

    pytest.main()
