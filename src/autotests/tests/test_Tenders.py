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

def test_open_all_objects(driver):
    driver.get(TendersPage.URL)
    tenders = TendersPage(driver)
    assert tenders.get_title() == 'Торги. Имущество - Инвестиционный портал Москвы'
    tenders.open_all_project()
    driver.close()

def test_rent_for_bissness(driver):
    driver.get(TendersPage.URL)
    tenders = TendersPage(driver)
    tenders.open_rent_for_bissness()
    driver.close()

def test_rent_for_bissness(driver):
    driver.get(TendersPage.URL)
    tenders = TendersPage(driver)
    tenders.open_rent_for_bissness()
    driver.close()