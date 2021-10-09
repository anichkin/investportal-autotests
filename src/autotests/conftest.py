import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--base_url',
        action='store',
        default='https://investmoscow.upt24.ru',
        help='base_url, avalible options: '+
             'https://investmoscow.upt24.ru, '+
             'https://new.investmoscow.upt24.ru, '+
             'https://new2.investmoscow.upt24.ru, '+
             'https://investmoscow.ru, '+
             'https://web1.investmoscow.ru, '+
             'https://web2.investmoscow.ru, '+
             'https://web3.investmoscow.ru, '+
             'https://web4.investmoscow.ru, '
    )


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()
