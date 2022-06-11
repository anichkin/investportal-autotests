from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage

class DGPMainPage(BasePage):
    PATH = ''
    HEADER_XPATH = (By.CSS_SELECTOR,'#LoginForm > fieldset > legend > div > span')
    HEADER = 'АИС УИД'
    LOGIN_INPUT = (By.CSS_SELECTOR,'#LoginTextBox')
    LOGIN = 'dgp_tester'
    PASSWORD = '4fO#@rpk'
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#PasswordTextBox')
    ENTER_BUTTON = (By.XPATH, '//*[@id="LoginForm"]/fieldset/div[4]/div/button[1]')
    TRADES_SUBSYSTEM_XPATH = '/html/body/div[2]/div/div/div[1]/a'
    TRADES_SUBSYSTEM = 'Подсистема имущественных торгов'
    LPO_SUBSYSTEM_XPATH = '/html/body/div[2]/div/div/div[2]/a'
    LPO_SUBSYSTEM = 'Подсистема обратной связи с инвесторами'
    SUBSIDY_SUBSYSTEM_XPATH = '/html/body/div[2]/div/div/div[3]/a'
    SUBSIDY_SUBSYSTEM = 'Подсистема заявок на субсидию'
    APPLICATIONS_SUBSYSTEM_XPATH = '/html/body/div[2]/div/div/div[4]/a'
    APPLICATIONS_SUBSYSTEM = 'Подсистема записи'






    def login(self):
        login_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(DGPMainPage.LOGIN_INPUT))
        login_input.send_keys(DGPMainPage.LOGIN)
        password_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(DGPMainPage.PASSWORD_INPUT))
        password_input.send_keys(DGPMainPage.PASSWORD)
        enter = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(DGPMainPage.ENTER_BUTTON))
        enter.click()



