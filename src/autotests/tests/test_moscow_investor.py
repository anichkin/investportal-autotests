from autotests.pages.MoscowInvestorPage import MoscowInvestorPage
import allure
import time
from autotests.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_main_page(driver, base_url):
    with allure.step('1. Открытие страницы Московский инвестор'):
        page = MoscowInvestorPage.open_mos_investor_page(driver, base_url)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Проверка наличия основных заголовков'):
        assert page.title == page.TITLE
        assert page.get_visible_by_xpath(page.HEADING_XPATH).text == page.HEADING
        assert page.get_visible_by_xpath(page.SUBTITLE_XPATH).text == page.SUBTITLE
        assert page.get_visible_by_xpath(page.HEADING2_XPATH).text == page.HEADING2
        assert page.get_visible_by_xpath(page.SUBTITLE2_XPATH).text == page.SUBTITLE2
        assert page.get_visible_by_xpath(page.SUBTITLE3_XPATH).text == page.SUBTITLE3
    with allure.step('3. Проверка классификатора'):
        page.get_clicable_by_xpath(page.CLASSIFICATOR_BUTTON).click()
        assert page.get_visible_by_xpath(page.HEADING3_XPATH).text == page.HEADING3
        assert page.get_visible_by_xpath(page.LAND_XPATH).text == page.LAND
        page.get_clicable_by_xpath(page.LAND_XPATH).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        assert page.get_visible_by_xpath(page.LAND_CATEGORY1_XPATH).text == page.LAND_CATEGORY1
        assert page.get_visible_by_xpath(page.PROBLEM_36_XPATH).text == page.PROBLEM_36
        assert page.get_visible_by_xpath(page.LAND_CATEGORY2_XPATH).text == page.LAND_CATEGORY2
        page.get_clicable_by_xpath(page.LAND_CATEGORY2_XPATH).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        assert page.get_visible_by_xpath(page.PROBLEM_38_XPATH).text == page.PROBLEM_38
        assert page.get_visible_by_xpath(page.PROBLEM_1_XPATH).text == page.PROBLEM_1
        assert page.get_visible_by_xpath(page.PROBLEM_47_XPATH).text == page.PROBLEM_47
        assert page.get_visible_by_xpath(page.PROBLEM_125_XPATH).text == page.PROBLEM_125
        assert page.get_visible_by_xpath(page.LAND_CATEGORY3_XPATH).text == page.LAND_CATEGORY3
        page.get_clicable_by_xpath(page.LAND_CATEGORY3_XPATH).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        assert page.get_visible_by_xpath(page.PROBLEM_39_XPATH).text == page.PROBLEM_39
        assert page.get_visible_by_xpath(page.PROBLEM_40_XPATH).text == page.PROBLEM_40
        assert page.get_visible_by_xpath(page.PROBLEM_42_XPATH).text == page.PROBLEM_42
        assert page.get_visible_by_xpath(page.REAL_ESTATE_XPATH).text == page.REAL_ESTATE
        page.get_clicable_by_xpath(page.REAL_ESTATE_XPATH).click()
        assert page.get_visible_by_xpath(page.REAL_ESTATE_CATEGORY1_XPATH).text == page.REAL_ESTATE_CATEGORY1
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

        assert page.get_visible_by_xpath(page.TENDERS_XPATH).text == page.TENDERS
        page.get_clicable_by_xpath(page.TENDERS_XPATH).click()

    with allure.step('4. Проверка блока предложения'):
        assert page.get_visible_by_xpath(page.PROPOSAL_XPATH).text == page.PROPOSAL
        assert page.get_visible_by_xpath(page.PROPOSAL_SUBTITLE_XPATH).text == page.PROPOSAL_SUBTITLE

    with allure.step('4. Проверка блока документации'):
        assert page.get_visible_by_xpath(page.FIRST_DOCUMENT_XPATH).text == page.FIRST_DOCUMENT
        #page.get_clicable_by_xpath(page.FIRST_DOCUMENT_XPATH).click()
        assert page.get_visible_by_xpath(page.SECOND_DOCUMENT_XPATH).text == page.SECOND_DOCUMENT
        #page.get_clicable_by_xpath(page.SECOND_DOCUMENT_XPATH).click()







