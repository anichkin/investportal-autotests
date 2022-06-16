from autotests.pages.PortalPages.MTSPages.MTSPage import MTSPage
from autotests.pages.PortalPages.MTSPages.MTSMembersPage import MTSMembersPage
from autotests.pages.PortalPages.MTSPages.MTSProgramPage import MTSProgramPage
import allure

def test_mts_page(driver, base_url):
    """Открытие главной страницы раздела МТШ"""
    with allure.step('1. Открыть информационную страницу МТШ, проверить элементы на странице'):
        page = MTSPage(driver, base_url)
        page.get()
        assert page.get_visible_by_xpath(page.HEADER_XPATH).text == page.HEADER
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Проверка раздела Проект позволит'):
        header = page.get_visible_by_xpath(page.HEADER2_XPATH)
        assert header.text == page.HEADER2
        header.location_once_scrolled_into_view
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('3. Переход на страницу Участникам'):
        button = page.get_clicable_by_xpath(page.MEMBERS_BUTTON)
        button.click()
        page = MTSMembersPage(driver, base_url)
        assert page.get_visible_by_xpath(page.HEADER_XPATH).text == page.HEADER
        assert page.get_visible_by_xpath(page.SUBTITLE_XPATH).text == page.SUBTITLE
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('4. Проверка блока РОЛИ И ЗАДАЧИ УЧАСТНИКОВ ЭКСПЕРТНОГО СОВЕТА'):
        header2 = page.get_visible_by_xpath(page.HEADER2_XPATH)
        assert header2.text == page.HEADER2
        header2.location_once_scrolled_into_view
        page.get_visible_by_xpath(page.ROLE1)
        page.get_visible_by_xpath(page.ROLE2)
        page.get_visible_by_xpath(page.ROLE3)
        page.get_visible_by_xpath(page.ROLE4)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('5. Переход на страницу программ'):
        page.get_clicable_by_xpath(page.PROGRAM_BUTTON).click()
        page = MTSProgramPage(driver, base_url)
        header = page.get_visible_by_xpath(page.HEADER_XPATH)
        assert header.text == page.HEADER
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('6. Переход к списку программ'):
        subtitle = page.get_visible_by_xpath(page.SUBTITLE_XPATH)
        assert subtitle.text == page.SUBTITLE
        subtitle.location_once_scrolled_into_view
        page.get_visible_by_xpath(page.PROGRAM1)
        page.get_visible_by_xpath(page.PROGRAM2)
        page.get_visible_by_xpath(page.PROGRAM3)
        page.get_visible_by_xpath(page.PROGRAM4)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")









