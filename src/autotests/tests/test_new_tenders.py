from autotests.pages import NewTendersPage
import allure


def test_page(driver, base_url):
    """
      Наименование сценария:
      Сценарий открытия торгов

      Шаг 1. Открытие главной страницы Имущество от города

          Открыть в браузере страницу https://investmoscow.ru/tenders

          Cтраница открылась


      Шаг 2. Выбор параметров в быстром фильтре

          Выбрать параметры Тип объекта и Вид торгов в быстром фильтре

          Параметры успешно выбраны

  """
    with allure.step('1. Открытие главной страницы Имущество от города'):
        page = NewTendersPage(driver, base_url)
        page.get()
        assert page.title == NewTendersPage.TITLE
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Выбор параметров в быстром фильтре'):
        page.select_object_types(['Квартира', 'Машино-место'])
        page.select_trade_types(['Продажа','Аренда'])
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")

