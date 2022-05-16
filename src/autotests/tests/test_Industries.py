import pytest
from selenium import webdriver
from autotests.pages.IndustriesPage import IndustriesPage
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


def test_blocks(driver, base_url):
    driver.get('https://investmoscow.ru/')
    driver.save_screenshot("/home/anichkin/Pictures/sobaka.png")
#    pageSource = driver.page_source
#    fileToWrite = open("/home/anichkin/Pictures/page_source.html", "w")
#    fileToWrite.write(pageSource)
#    fileToWrite.close()
#    fileToRead = open("/home/anichkin/Pictures/page_source.html", "r")
#    print(fileToRead.read())
#    fileToRead.close()
#    driver.quit()
    industries = IndustriesPage(driver, base_url)
    industries.get()
    industries.check_blocks()






if __name__ == "__main__":

    pytest.main()
