from autotests.pages.online_services_page import OnlineServicesPage
import allure
import time


def test_online_services(driver, base_url, block=OnlineServicesPage.HEADER_XPATH):
    with allure.step('1. Открыть страницу онлайн сервисов'):
        page = OnlineServicesPage.open_online_services_page(driver, base_url, block)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Проверка наличия основных элементов на странице'):
        assert page.title == OnlineServicesPage.TITLE
        assert page.get_visible_by_xpath(page.HEADER_XPATH).text == page.HEADER
        assert page.get_visible_by_xpath(page.SUBTITLE_XPATH).text == page.SUBTITLE
        page.get_visible_by_xpath(page.SCROLL_BAR)

def test_direct_connection(driver, base_url, block=OnlineServicesPage.DIRECT_CONNECTION):
    with allure.step('1. Перейти к блоку Прямая связь'):
        page = OnlineServicesPage.open_online_services_page(driver, base_url, block)
        page.get_clicable_by_css(page.DIRECT_CONNECTION).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Раскрыть полный список сервисов в блоке'):
        page.get_clicable_by_xpath(page.DIRECT_CONNECTION_FULL_LIST).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('3. Проверить наличие элементов в блоке'):
        assert page.get_visible_by_xpath(page.DIRECT_CONNECTION_HEADER_XPATH).text == page.DIRECT_CONNECTION_HEADER
        assert page.get_visible_by_xpath(page.DIRECT_CONNECTION_SUBTITLE_XPATH).text == page.DIRECT_CONNECTION_SUBTITLE
        assert page.get_visible_by_xpath(page.DIRECT_CONNECTION_HEADER2_XPATH).text == page.DIRECT_CONNECTION_HEADER2
        with allure.step('Проверка ЛПО'):
            assert page.get_visible_by_xpath(page.LPO_BLOCK_XPATH).text == page.LPO_BLOCK
            assert page.get_visible_by_xpath(page.LPO_SUBTITLE_XPATH).text == page.LPO_SUBTITLE
            assert page.get_clicable_by_xpath(page.LPO_BUTTON_XPATH).text == page.LPO_BUTTON
        with allure.step('Проверка московского инвестора'):
             assert page.get_visible_by_xpath(page.MOS_INVESTOR_HEADER_XPATH).text == page.MOS_INVESTOR_HEADER
             assert page.get_visible_by_xpath(page.MOS_INVESTOR_SUBTITLE_XPATH).text == page.MOS_INVESTOR_SUBTITLE
             assert page.get_clicable_by_xpath(page.MOS_INVESTOR_BUTTON_XPATH).text == page.MOS_INVESTOR_BUTTON
        with allure.step('Проверка блока Ковид'):
            assert page.get_visible_by_xpath(page.COVID_HEADER_XPATH).text == page.COVID_HEADER
            assert page.get_visible_by_xpath(page.COVID_SUBTITLE_XPATH).text == page.COVID_SUBTITLE
            assert page.get_clicable_by_xpath(page.COVID_BUTTON_XPATH).text == page.COVID_BUTTON
        with allure.step('Проверка блока информкиоска'):
            assert page.get_visible_by_xpath(page.INFORM_KIOSK_HEADER_XPATH).text == page.INFORM_KIOSK_HEADER
            assert page.get_visible_by_xpath(page.INFORM_KIOSK_SUBTITLE_XPATH).text == page.INFORM_KIOSK_SUBTITLE
            assert page.get_clicable_by_xpath(page.INFORM_KIOSK_BUTTON_XPATH).text == page.INFORM_KIOSK_BUTTON







