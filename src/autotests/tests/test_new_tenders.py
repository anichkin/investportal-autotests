
from autotests.pages import NewTendersPage
import allure
import time


def test_page(driver, base_url):
    """
      Наименование сценария:
      Сценарий открытия торгов

      Шаг 1. Открытие главной страницы Имущество от города

          Открыть в браузере страницу https://investmoscow.ru/tenders

          Cтраница открылась

      Шаг 2. Проверка наличия новых и популярных торгов на странице

          Проверить наличие элементов на странице

          Элементы присутсвуют

      Шаг 3. Выбор параметров в быстром фильтре

          Выбрать параметры Тип объекта и Вид торгов в быстром фильтре

          Параметры успешно выбраны

  """
    with allure.step('1. Открытие главной страницы Имущество от города'):
        page = NewTendersPage(driver, base_url)
        page.get()
        assert page.title == NewTendersPage.TITLE
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

    with allure.step('2. Проверка наличия загрузки новых тендеров и популярных объектов'):
        page.get_visible_by_css(page.FIRST_NEW_TENDER)
        page.get_visible_by_css(page.SECOND_NEW_TENDER)
        page.get_visible_by_css(page.THIRD_NEW_TENDER)
        #driver.execute_script("window.scrollTo(0, 1460)")
        #page.get_visible_by_css(page.FIRST_POPULAR_TENDER)
        #page.get_visible_by_css(page.SECOND_POPULAR_TENDER)
        #page.get_visible_by_css(page.THIRD_POPULAR_TENDER)


    with allure.step('3. Выбор параметров в быстром фильтре'):
        page.select_object_types(['Квартира', 'Машино-место', 'Нежилые помещения'])
        page.select_trade_types(['Продажа','Аренда'])
        search = page.get_clicable_by_css(page.SEARCH_BUTTON)
        search.click()
        page.get_visible_by_xpath(page.WIDE_FILTER_XPATH)
        assert page.get_visible_by_xpath(page.WIDE_FILTER_XPATH).text == page.WIDE_FILTER
        try:
            page.get_visible_by_css(page.FIRST_SEARCH_RESULT_TENDER1)
        except Exception:
            page.get_visible_by_css(page.FIRST_SEARCH_RESULT_TENDER2)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")



def test_tender(driver, base_url):
    """Открытие подробной карточки торгов и проверка наличия элементов внутри"""

    with allure.step('1. Открытие страницы торгов и переход к основному списку'):
        page = NewTendersPage(driver, base_url)
        page.get()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        time.sleep(2)
        all_object_navigation = page.get_visible_by_xpath(page.NAVIGATION)
        all_object_navigation.location_once_scrolled_into_view
        time.sleep(1)
        try:
            page.get_clicable_by_css(page.ALL_OBJECT_BUTTON).click()
        except Exception:
            page.get_visible_by_xpath(page.ALL_OBJECT_BUTTON_XPATH)
            page.get_clicable_by_xpath(page.ALL_OBJECT_BUTTON_XPATH).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")


    with allure.step('2.Открытие подробной страницы торгов'):
        try:
            driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
            time.sleep(2)
            page.get_visible_by_css(page.FIRST_SEARCH_RESULT_TENDER1).click()
            page.get_clicable_by_css(page.COLLAPSE_TENDERS).click()
            tender = page.get_clicable_by_css(page.FIRST_COLLAPSE_TENDER).location_once_scrolled_into_view
            tender.click()
        except Exception:
            driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
            time.sleep(2)
            page.get_visible_by_css(page.FIRST_SEARCH_RESULT_TENDER2).click()
        handle = driver.window_handles
        driver.switch_to.window(handle[1])
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

    with allure.step('3. Проверка элементов на карточке торгов'):
        with allure.step('Проверка наличия карты и раскрытия документов'):
            map = page.get_visible_by_xpath(page.MAP)
            try:
                page.get_visible_by_xpath(page.DOCUMENT_BUTTON).location_once_scrolled_into_view
                page.get_clicable_by_xpath(page.DOCUMENT_BUTTON).click()
                page.get_visible_by_xpath(page.OBJECT_DOCUMENT).location_once_scrolled_into_view
                page.get_clicable_by_xpath(page.OBJECT_DOCUMENT).click()
                page.get_visible_by_xpath(page.TENDER_DOCUMENT).location_once_scrolled_into_view
                page.get_clicable_by_xpath(page.TENDER_DOCUMENT).click()
            except Exception:
                page.get_visible_by_xpath(page.DOCUMENT_BUTTON_2).location_once_scrolled_into_view
                page.get_clicable_by_xpath(page.DOCUMENT_BUTTON_2).click()
                page.get_visible_by_xpath(page.OBJECT_DOCUMENT_2).location_once_scrolled_into_view
                page.get_clicable_by_xpath(page.OBJECT_DOCUMENT_2).click()
                page.get_visible_by_xpath(page.TENDER_DOCUMENT_2).location_once_scrolled_into_view
                page.get_clicable_by_xpath(page.TENDER_DOCUMENT_2).click()
            map.location_once_scrolled_into_view
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        with allure.step('Проверка блока информации о торгах'):
            subject_tabs = page.get_visible_by_xpath(page.SUBJECT_TABS)
            subject_tabs.location_once_scrolled_into_view
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        with allure.step('Проверка блока похожих объектов'):
            try:
                simular_objects = page.get_visible_by_xpath(page.SIMULAR_OBJECTS)
                simular_objects.location_once_scrolled_into_view
                allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
            except Exception:
                print('Блока похожих объектов нет')
        with allure.step('Проверка блока мероприятий'):
            events = page.get_visible_by_xpath(page.EVENTS)
            events.location_once_scrolled_into_view
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")





