import pytest
from selenium import webdriver
from datetime import datetime
import allure
import time



def pytest_addoption(parser):
    parser.addoption(
        '--base_url',
        action='store',
        default='https://investmoscow.ru',
        help='base_url, available options: '+
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
    #options.add_argument('--no-sandbox')
    #    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--incognito')
    options.add_argument('window-size=1920x1080')
    #options.add_argument("--start-maximized")
    # options.add_argument("--screenshot")
    #    options.add_experimental_option('useAutomationExtension', False)
    #    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['driver']
            allure.attach(driver.get_screenshot_as_png(), name="Error")
            webdriver.save_screenshot('/error_screenshots/error.png')
            print("executing test failed", request.node.nodeid)

