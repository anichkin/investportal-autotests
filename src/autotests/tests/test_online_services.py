from autotests.pages.PortalPages.online_services_page import OnlineServicesPage
import allure


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

def test_services(driver, base_url, block = OnlineServicesPage.SERVICES):
    with allure.step('1. Перейти к блоку Услуги'):
        page = OnlineServicesPage.open_online_services_page(driver, base_url, block)
        page.get_clicable_by_css(page.SERVICES).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Раскрыть полный список сервисов'):
        page.get_clicable_by_xpath(page.SERVICES_FULL_LIST).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('3. Проверить наличие элементов в блоке'):
        assert page.get_visible_by_xpath(page.SERVICES_HEADER_XPATH).text == page.SERVICES_HEADER
        assert page.get_visible_by_xpath(page.SERVICES_SUBTITLE_XPATH).text == page.SERVICES_SUBTITLE
        assert page.get_visible_by_xpath(page.SERVICES_HEADER2_XPATH).text == page.SERVICES_HEADER2
        with allure.step('Проверка НАПРАВИТЬ ИНВЕСТИЦИОННЫЙ ПРОЕКТ'):
            assert page.get_visible_by_xpath(page.INVEST_PROJECT_HEADER_XPATH).text == page.INVEST_PROJECT_HEADER
            assert page.get_visible_by_xpath(page.INVEST_PROJECT_SUBTITLE_XPATH).text == page.INVEST_PROJECT_SUBTITLE
            assert page.get_clicable_by_xpath(page.INVEST_PROJECT_BUTTON_XPATH).text == page.INVEST_PROJECT_BUTTON
        with allure.step('Проверка АРЕНДА ПОМЕЩЕНИЙ В ТЕХНОПАРКАХ'):
             assert page.get_visible_by_xpath(page.RENT_ROOM_HEADER_XPATH).text == page.RENT_ROOM_HEADER
             assert page.get_visible_by_xpath(page.RENT_ROOM_SUBTITLE_XPATH).text == page.RENT_ROOM_SUBTITLE
             assert page.get_clicable_by_xpath(page.RENT_ROOM_BUTTON_XPATH).text == page.RENT_ROOM_BUTTON
        with allure.step('Проверка ЗАЯВКА НА ПОДБОР ПРОМЫШЛЕННОЙ ПЛОЩАДКИ'):
            assert page.get_visible_by_xpath(page.REQUEST_FOR_AREA_HEADER_XPATH).text == page.REQUEST_FOR_AREA_HEADER
            assert page.get_visible_by_xpath(page.REQUEST_FOR_AREA_SUBTITLE_XPATH).text == page.REQUEST_FOR_AREA_SUBTITLE
            assert page.get_clicable_by_xpath(page.REQUEST_FOR_AREA_BUTTON_XPATH).text == page.REQUEST_FOR_AREA_BUTTON
        with allure.step('Проверка ВКЛЮЧЕНИЕ В РЕЕСТР ПРОМПЛОЩАДОК'):
            assert page.get_visible_by_xpath(page.INCLUDING_IN_REESTR_HEADER_XPATH).text == page.INCLUDING_IN_REESTR_HEADER
            assert page.get_visible_by_xpath(page.INCLUDING_IN_REESTR_SUBTITLE_XPATH).text == page.INCLUDING_IN_REESTR_SUBTITLE
            assert page.get_clicable_by_xpath(page.INCLUDING_IN_REESTR_BUTTON_XPATH).text == page.INCLUDING_IN_REESTR_BUTTON
        with allure.step('Проверка НАПРАВИТЬ КОНЦЕССИОННУЮ ИНИЦИАТИВУ'):
            assert page.get_visible_by_xpath(page.CONCESSION_INITIATIVE_HEADER_XPATH).text == page.CONCESSION_INITIATIVE_HEADER
            assert page.get_visible_by_xpath(page.CONCESSION_INITIATIVE_SUBTITLE_XPATH).text == page.CONCESSION_INITIATIVE_SUBTITLE
            assert page.get_clicable_by_xpath(page.CONCESSION_INITIATIVE_BUTTON_XPATH).text == page.CONCESSION_INITIATIVE_BUTTON
        with allure.step('Проверка ИВЕСТИЦИОННЫЙ КАТАЛОГ'):
            assert page.get_visible_by_xpath(page.INVEST_CATALOG_HEADER_XPATH).text == page.INVEST_CATALOG_HEADER
            assert page.get_visible_by_xpath(page.INVEST_CATALOG_SUBTITLE_XPATH).text == page.INVEST_CATALOG_SUBTITLE
            assert page.get_clicable_by_xpath(page.INVEST_CATALOG_BUTTON_XPATH).text == page.INVEST_CATALOG_BUTTON











