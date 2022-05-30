
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
        page.select_object_types(['Квартира', 'Машино-место'])
        page.select_trade_types(['Продажа','Аренда'])
        page.get_clicable_by_css(page.SEARCH_BUTTON).click()
        page.get_visible_by_xpath(page.WIDE_FILTER_XPATH)
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
        third_tender = page.get_visible_by_xpath(page.NAVIGATION)
        third_tender.location_once_scrolled_into_view
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        page.get_clicable_by_css(page.ALL_OBJECT_BUTTON).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")


    with allure.step('2.Открытие подробной страницы торгов'):
        try:
            page.get_clicable_by_css(page.FIRST_SEARCH_RESULT_TENDER1).location_once_scrolled_into_view
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
            page.get_clicable_by_css(page.FIRST_SEARCH_RESULT_TENDER1).click()
            page.get_clicable_by_css(page.COLLAPSE_TENDERS).click()
            page.get_clicable_by_css(page.FIRST_COLLAPSE_TENDER).click()
        except Exception:
            page.get_clicable_by_css(page.FIRST_SEARCH_RESULT_TENDER2).location_once_scrolled_into_view
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
            page.get_clicable_by_css(page.FIRST_SEARCH_RESULT_TENDER2).click()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        handle = driver.window_handles
        driver.switch_to.window(handle[1])
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

    with allure.step('3. Проверка элементов на карточке торгов'):
        with allure.step('Проверка наличия карты и раскрытия документов'):
         map = page.get_visible_by_xpath(page.MAP)
         page.get_clicable_by_xpath(page.DOCUMENT_BUTTON).click()
         page.get_clicable_by_xpath(page.OBJECT_DOCUMENT).click()
         page.get_clicable_by_xpath(page.TENDER_DOCUMENT).click()
         map.location_once_scrolled_into_view
         allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        with allure.step('Проверка блока информации о торгах'):
         subject_tabs = page.get_visible_by_xpath(page.SUBJECT_TABS)
         subject_tabs.location_once_scrolled_into_view
         allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        with allure.step('Проверка блока похожих объектов'):
         simular_objects = page.get_visible_by_xpath(page.SIMULAR_OBJECTS)
         simular_objects.location_once_scrolled_into_view
         allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        with allure.step('Проверка блока мероприятий'):
         events = page.get_visible_by_xpath(page.EVENTS)
         events.location_once_scrolled_into_view
         allure.attach(driver.get_screenshot_as_png(), name="Screenshot")





