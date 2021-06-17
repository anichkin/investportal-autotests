import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.TendersPage import TendersPage



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def test_open_pages(driver, page, url, text):
    driver.get(TendersPage.URL)
    tenders = TendersPage(driver)
    assert tenders.get_title() == 'Торги. Имущество - Инвестиционный портал Москвы'
    tenders.open_page(page)
    assert driver.current_url == url
    assert text == driver.find_element_by_xpath('//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    driver.close()

# def test_rent_for_bissness():
#     driver.get(TendersPage.URL)
#     tenders = TendersPage.driver
#     tenders.



# def test_rent_for_bissness(driver):
#     driver.get(TendersPage.URL)
#     tenders = TendersPage(driver)
#     tenders.open_rent_for_bissness()
#     driver.close()