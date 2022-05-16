import pytest
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
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
    #options.add_argument("--screenshot")
#    options.add_experimental_option('useAutomationExtension', False)
#    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome(options=options)
