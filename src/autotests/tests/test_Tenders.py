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



# def test_open_pages(driver, page, url, text):
#     driver.get(TendersPage.URL)
#     tenders = TendersPage(driver)
#     assert tenders.get_title() == 'Торги. Имущество - Инвестиционный портал Москвы'
#     tenders.open_page(page)
#     assert driver.current_url == url
#     assert text == driver.find_element_by_xpath('//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
#     driver.close()

# def test_rent_for_bissness():
#     driver.get(TendersPage.URL)
#     tenders = TendersPage.driver
#     tenders.

def test_open_all_objects(driver):
    tenders = TendersPage.open_tender_page(driver)
    assert TendersPage.open_tender_page(driver).get_title() == 'Торги. Имущество - Инвестиционный портал Москвы'
    tenders.open_all_project()
    assert driver.current_url == TendersPage.URL_ALL_OBJECTS
    assert TendersPage.TEXT_ALL_OBJECTS == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    driver.close()

def test_rent_for_bissness(driver):
    tenders = TendersPage.open_tender_page(driver)
    assert TendersPage.open_tender_page(driver).get_title() == 'Торги. Имущество - Инвестиционный портал Москвы'
    tenders.open_rent_for_bissness_all()
    assert driver.current_url == TendersPage.URL_RENT_FOR_BISSNESS_ALL
    assert TendersPage.TEXT_RENT_FOR_BISSNESS_ALL == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_rent_for_bissness_room()
    assert driver.current_url == TendersPage.URL_RENT_FOR_BISSNESS_ROOM
    assert TendersPage.TEXT_RENT_FOR_BISSNESS_ROOM == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_rent_for_bissness_building()
    assert driver.current_url == TendersPage.URL_RENT_FOR_BISSNESS_BUILDING
    assert TendersPage.TEXT_RENT_FOR_BISSNESS_BUILDING == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_rent_for_bissness_structure()
    assert driver.current_url == TendersPage.URL_RENT_FOR_BISSNESS_STRUCTURE
    assert TendersPage.TEXT_RENT_FOR_BISSNESS_STRUCTURE == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)
    driver.close()

def test_sale_for_bissness(driver):
    tenders = TendersPage.open_tender_page(driver)
    assert TendersPage.open_tender_page(driver).get_title() == 'Торги. Имущество - Инвестиционный портал Москвы'
    tenders.open_sale_for_bissness_all_objects()
    assert driver.current_url == TendersPage.URL_SALE_FOR_BISSNESS_ALL_OBJECTS
    assert TendersPage.TEXT_SALE_FOR_BISSNESS_ALL_OBJECTS == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_sale_for_bissness_premises()
    assert driver.current_url == TendersPage.URL_SALE_FOR_BISSNESS_PREMISES
    assert TendersPage.TEXT_SALE_FOR_BISSNESS_PREMISES == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_sale_for_bissness_building()
    assert driver.current_url == TendersPage.URL_SALE_FOR_BISSNESS_BUILDING
    assert TendersPage.TEXT_SALE_FOR_BISSNESS_BUILDING == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_sale_for_bissness_structure()
    assert driver.current_url == TendersPage.URL_SALE_FOR_BISSNESS_STRUCTURE
    assert TendersPage.TEXT_SALE_FOR_BISSNESS_STRUCTURE == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_sale_for_bissness_non_finished()
    assert driver.current_url == TendersPage.URL_SALE_FOR_BISSNESS_NON_FINISHED
    assert TendersPage.TEXT_SALE_FOR_BISSNESS_NON_FINISHED == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_sale_for_bissness_land_and_building()
    assert driver.current_url == TendersPage.URL_SALE_FOR_BISSNESS_LAND_AND_BUILDING
    assert TendersPage.TEXT_SALE_FOR_BISSNESS_LAND_AND_BUILDING == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_sale_for_bissness_stock()
    assert driver.current_url == TendersPage.URL_SALE_FOR_BISSNESS_STOCK
    assert TendersPage.TEXT_SALE_FOR_BISSNESS_STOCK == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)
    driver.close()

def test_land_for_building(driver):
    tenders = TendersPage.open_tender_page(driver)
    assert TendersPage.open_tender_page(driver).get_title() == 'Торги. Имущество - Инвестиционный портал Москвы'
    tenders.open_land_for_building()
    assert driver.current_url == TendersPage.URL_LAND_FOR_BUILDING
    assert TendersPage.TEXT_LAND_FOR_BUILDING == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    driver.close()

def test_for_people(driver):
    tenders = TendersPage.open_tender_page(driver)
    assert TendersPage.open_tender_page(driver).get_title() == 'Торги. Имущество - Инвестиционный портал Москвы'
    tenders.open_for_people_all_objects()
    assert driver.current_url == TendersPage.URL_FOR_PEOPLE_ALL_OBJECTS
    assert TendersPage.TEXT_FOR_PEOPLE_ALL_OBJECTS == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_for_people_flat()
    assert driver.current_url == TendersPage.URL_FOR_PEOPLE_FLAT
    assert TendersPage.TEXT_FOR_PEOPLE_FLAT == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_for_people_room()
    assert driver.current_url == TendersPage.URL_FOR_PEOPLE_ROOM
    assert TendersPage.TEXT_FOR_PEOPLE_ROOM == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_for_people_path_of_flat()
    assert driver.current_url == TendersPage.URL_FOR_PEOPLE_PATH_OF_FLAT
    assert TendersPage.TEXT_FOR_PEOPLE_PATH_OF_FLAT == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_for_people_land_ijs()
    assert driver.current_url == TendersPage.URL_FOR_PEOPLE_LAND_IJS
    assert TendersPage.TEXT_FOR_PEOPLE_LAND_IJS == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)

    tenders.open_for_people_parking()
    assert driver.current_url == TendersPage.URL_FOR_PEOPLE_PARKING
    assert TendersPage.TEXT_FOR_PEOPLE_PARKING == driver.find_element_by_xpath(
        '//*[@id="property-objects"]/div/div[1]/div[1]/div/h2').text
    TendersPage.return_to_tenders(tenders)
    driver.close()


# def test_rent_for_bissness(driver):
#     driver.get(TendersPage.URL)
#     tenders = TendersPage(driver)
#     tenders.open_rent_for_bissness()
#     driver.close()
#
# def test_rent_for_bissness(driver):
#     driver.get(TendersPage.URL)
#     tenders = TendersPage(driver)
#     tenders.open_rent_for_bissness()
#     driver.close()
