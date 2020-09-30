import pytest
from selenium import webdriver
from autotests.pages.MainPage import MainPage
from autotests.pages.OnlineServicesPage import OnlineServicesPage


@pytest.fixture()
def current_dir():
    yield 'test_dir'


def test_login(current_dir):
    '''Функция теста логина и пароля'''
    print(current_dir)
    # Опция вебдрайвера
    options = webdriver.ChromeOptions()
    # Опция вебдрайвера для открытия полноэкранного режима
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    # Переходим на url
    driver.get(MainPage.URL)
    # Создание объекта класса mainpage
    main_page = MainPage(driver)
    # Сравниваем тайтл страницы
    assert main_page.get_title() == MainPage.TITLE
    # Проверяем авторизацию
    main_page.login()
    # Проверяем совпадает ли пользователь
    assert main_page.get_header_user_name() == 'Иванов44 И. И.'
    

def test_go_to_online_services_page():
    '''Переход в Онлайн сервисы'''

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(MainPage.URL)
    main_page = MainPage(driver)
    main_page.go_to_online_services_page()
    online_services_page = OnlineServicesPage(main_page.driver)
    assert online_services_page.get_title() == OnlineServicesPage.TITLE



def test_open_el_sliders():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(MainPage.URL2)
    main_page = MainPage(driver)
    


if __name__ == "__main__":

    pytest.main()