import pytest
from selenium import webdriver
from autotests.pages.main_page import MainPage
from autotests.pages.online_services_page import OnlineServicesPage


def test_login(driver, base_url):
    main_page = MainPage(driver, base_url)
    print(main_page.url)
    main_page.get()
    # Сравниваем тайтл страницы
    assert main_page.get_title() == MainPage.TITLE
    # Проверяем авторизацию
    main_page.login()
    # Проверяем совпадает ли пользователь
    assert main_page.get_header_user_name() == 'Иванов44 И. И.'
    

def test_go_to_online_services_page(driver, base_url):
    '''Переход в Онлайн сервисы'''
    main_page = MainPage(driver, base_url)
    main_page.get()
    main_page.go_to_online_services_page()
    online_services_page = OnlineServicesPage(driver, base_url)
    assert online_services_page.get_title() == OnlineServicesPage.TITLE


# def test_open_el_sliders(driver, base_url):
#     main_page = MainPage(driver, base_url)
#     main_page.get()
