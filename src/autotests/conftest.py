import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--base_url',
        action='store',
        default='https://investmoscow.ru',
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
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--headless')
    #    options.add_argument('--disable-blink-features=AutomationControlled')
    #    options.add_argument("--disable-extensions")
    options.add_argument('--no-sandbox')
    #    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")
    # options.add_argument("--screenshot")
    #    options.add_experimental_option('useAutomationExtension', False)
    #    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()
