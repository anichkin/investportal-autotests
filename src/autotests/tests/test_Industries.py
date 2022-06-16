import pytest
from autotests.pages.PortalPages.IndustriesPage import IndustriesPage
import allure



def test_blocks(driver, base_url):
    """ Открытие раздела промышленности и проверка наличия блоков """

    with allure.step('Открытие страницы раздела промышленности'):
        industries = IndustriesPage(driver, base_url)
        industries.get()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('Проверка заголовка страницы'):
        assert industries.title == industries.TITLE
    with allure.step('Проверка наличия блоков в разделе промышленности'):
        industries.check_blocks()






if __name__ == "__main__":

    pytest.main()
