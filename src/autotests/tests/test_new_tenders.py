import time
from autotests.pages import NewTendersPage


def test_page(driver, base_url):
    page = NewTendersPage(driver, base_url)
    page.get()
    assert page.title == NewTendersPage.TITLE
    page.select_object_types(['Квартира', 'Машино-место'])
    page.select_trade_types(['Продажа'])
    time.sleep(5)
