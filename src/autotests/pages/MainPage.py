from selenium.webdriver.common.by import By


class MainPage:

    URL = 'https://investmoscow.upt24.ru/'
    LOGIN_PIC = (By.XPATH, '//*[@id="auth-bt"]/a')

    def __init__(self, driver):

        self.driver = driver
        self.driver.get(MainPage.URL)

    def get_title(self):
        return self.driver.title

    def press_to_login_pic(self):
        login_pic = self.driver.find_element(*MainPage.LOGIN_PIC)
        login_pic.click()