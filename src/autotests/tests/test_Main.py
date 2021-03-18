import allure
import pytest
from selenium import webdriver
from autotests.pages.MainPage import MainPage
from autotests.pages.OnlineServicesPage import OnlineServicesPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


# def test_login(driver):
#     '''Функция теста логина и пароля'''
#
#     # Переходим на url
#     driver.get(MainPage.URL)
#     # Создание объекта класса mainpage
#     main_page = MainPage(driver)
#     # Сравниваем тайтл страницы
#     assert main_page.get_title() == MainPage.TITLE
#     # Проверяем авторизацию
#     main_page.login()
#     # Проверяем совпадает ли пользователь
#     assert main_page.get_header_user_name() == 'Иванов44 И. И.'
    

# def test_go_to_online_services_page(driver):
#     '''Переход в Онлайн сервисы'''
#
#     driver.get(MainPage.URL2)
#     main_page = MainPage(driver)
#     main_page.go_to_online_services_page()
#     online_services_page = OnlineServicesPage(main_page.driver)
#     assert online_services_page.get_title() == OnlineServicesPage.TITLE



def test_open_el_sliders(driver):

    driver.get(MainPage.URL)
    main_page = MainPage(driver)
    


if __name__ == "__main__":

    pytest.main()