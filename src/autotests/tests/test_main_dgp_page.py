import pytest
from autotests.pages.DGPMainPage import DGPMainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure





def test_dgp_authorization(driver, dgp_base_url):
    """тест авторизации"""
    page = DGPMainPage(driver, dgp_base_url)
    page.get()
    page.login()

def test_dashboard(driver, dgp_base_url):
    """Проверка элементов дашборда"""
    with allure.step('Проверка наличия элементов на странице'):
        page = DGPMainPage(driver, dgp_base_url)
        page.get()
        assert page.get_visible_by_xpath(page.TRADES_SUBSYSTEM_XPATH).text == page.TRADES_SUBSYSTEM
        assert page.get_visible_by_xpath(page.LPO_SUBSYSTEM_XPATH).text == page.LPO_SUBSYSTEM
        assert page.get_visible_by_xpath(page.SUBSIDY_SUBSYSTEM_XPATH).text == page.SUBSIDY_SUBSYSTEM
        assert page.get_visible_by_xpath(page.APPLICATIONS_SUBSYSTEM_XPATH).text == page.APPLICATIONS_SUBSYSTEM
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")





