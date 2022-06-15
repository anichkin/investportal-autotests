from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    PATH=''
    WAIT_TIME = 10

    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url + self.__class__.PATH
    
    def get(self):
        self.driver.get(self.url)

    @property
    def title(self):
        return self.driver.title

    def get_visible_by_xpath(self, xpath: str) -> WebElement:
        return WebDriverWait(self.driver, self.__class__.WAIT_TIME).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def get_visible_by_css(self, css: str) -> WebElement:
        return WebDriverWait(self.driver, self.__class__.WAIT_TIME).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css))
        )

    def get_clicable_by_xpath(self, xpath: str) -> WebElement:
        return WebDriverWait(self.driver, self.__class__.WAIT_TIME).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    def get_clicable_by_css(self, css: str) -> WebElement:
        return WebDriverWait(self.driver, self.__class__.WAIT_TIME).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css))
        )

    def get_clicable_by_name(self, name: str) -> WebElement:
        return WebDriverWait(self.driver, self.__class__.WAIT_TIME).until(
            EC.element_to_be_clickable((By.NAME, name))
        )
