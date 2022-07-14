from autotests.pages.DGPPages.DGPSubjectReestrPage import DGPSubjectReestrPage
import  allure
from autotests.pages.DGPPages.DGPMainPage import DGPMainPage
import time
from flaky import flaky


@flaky
def test_open_subject_registry(driver, dgp_base_url):
    """Открытие реестра субъектов
        Фильтрация субъектов по объектам недвижимости
        Переход в первый отфильтрованный субъект
        Проверка возможности нажать кнопки запроса выписки и скачивания
        проверка хотя бы одного объекта недвижимости в субъекте
    """
    with allure.step('1. Авторизация в дгп'):
        page = DGPMainPage(driver, dgp_base_url)
        page.get()
        page.login()
        time.sleep(1)
    with allure.step('2. Открытие страницы реестра субъектов'):
        page = DGPSubjectReestrPage(driver, dgp_base_url)
        page.get()
        header = page.get_visible_by_xpath(page.HEADER_XPATH)
        assert header.text == page.HEADER
        page.get_visible_by_css(page.CARDS_AREA)
        page.get_visible_by_css(page.FIRST_CARD)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('3. Проверить наличие кнопки выписки объектов недвижимости'):
        with allure.step('Фильтрация объектов недвижимости'):
            filter = page.get_clicable_by_css(page.FILTER_AREA)
            filter.click()
            checkbox = page.get_clicable_by_css(page.CHECKBOX)
            checkbox.click()
            enter = page.get_clicable_by_css(page.ENTER_BUTTON)
            enter.click()
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        with allure.step('Открытие первой карточки, проверка кнопок запроса выписки и скачивания'):
            first_card = page.get_visible_by_css(page.FIRST_CARD)
            first_card.click()
            handle = driver.window_handles
            driver.switch_to.window(handle[1])
            request_for_doc = page.get_visible_by_css(page.REQUEST_FOR_DOC_CSS)
            assert request_for_doc.text == page.REQUEST_FOR_DOC
            download = page.get_visible_by_css(page.DOWNLOAD_BUTTON_CSS)
            assert download.text == page.DOWNLOAD_BUTTON
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        with allure.step('Переход на вкладку Объекты недвижимости, проверка наличия хотя бы одного объекта'):
            property_tab = page.get_clicable_by_xpath(page.PROPERTY_TAB)
            property_tab.click()
            page.get_visible_by_css(page.FIRST_PROPERTY)
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")





