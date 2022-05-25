
from autotests.pages import NewTendersPage
import allure


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
        page.get_clicable_by_css(page.ALL_OBJECT_BUTTON).click()

    with allure.step('2.Открытие подробной страницы торгов'):
        try:
            page.get_clicable_by_css(page.FIRST_SEARCH_RESULT_TENDER1).click()
        except Exception:
            page.get_clicable_by_css(page.FIRST_SEARCH_RESULT_TENDER2).click()

    # with allure.step('3. Проверка элементов на карточке торгов'):
    #     page.get_visible_by_xpath(page.MAP)



