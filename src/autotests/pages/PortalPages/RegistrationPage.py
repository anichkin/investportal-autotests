from autotests.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class RegistrationPage(BasePage):
    PATH = '/Account/Register'
    TITLE = 'Регистрация - Инвестиционный портал Москвы'
    UL_XPATH = '//*[@id="type-user"]/div/div[1]/div/div/div[1]/label'
    UL = 'Юридическое лицо'
    NEXT1_BUTTON = '//*[@id="type-user"]/div/div[2]/a'
    LAST_NAME_XPATH = '//*[@id="Contact_SurName"]'
    LAST_NAME = 'Сидоров'
    NAME_XPATH = '//*[@id="Contact_Name"]'
    NAME = 'Алексей'
    MIDDLE_NAME_XPATH = '//*[@id="Contact_MiddleName"]'
    MIDDLE_NAME = 'Викторович'
    POSITION_XPATH = '//*[@id="Contact_Position"]'
    POSITION = 'Директор'
    PHONE_XPATH = '//*[@id="Contact_Phone"]'
    PHONE = '89454567634'
    EMAIL_XPATH = '//*[@id="Contact_Email"]'
    EMAIL = 'test_registration@upt24.ru'
    INDEX_XPATH = '//*[@id="Index"]'
    INDEX = '456123'
    FACT_ADRESS_XPATH = '//*[@id="FactAddress"]'
    FACT_ADRESS = 'г. Москва, Петровско-разумовский проезд, дом 8'
    INN_XPATH = '//*[@id="Inn"]'
    INN = '7142438762'
    NEXT2_BUTTON = '//*[@id="PersonalNext"]'
    OPF_XPATH = '//*[@id="typeUR"]'
    OPF = '6'
    ORG_NAME_XPATH = '//*[@id="OrgName"]'
    ORG_NAME = 'Uptime 24'
    LEGAL_ADRESS_XPATH = '//*[@id="jur2"]'
    LEGAL_ADRESS = 'г. Москва, Зеленоград, улица Гоголя 2'
    NEXT3_BUTTON = '//*[@id="UrPwNext"]'
    PASSWORD_XPATH = '//*[@id="passUser"]'
    REPEAT_PASSWORD_XPATH = '//*[@id="repPassUser"]'
    PASSWORD = 'qweQWE123!'
    PASSWORD_FAQ_XPATH = '//*[@id="password-user"]/div/div[1]/div/div/div[2]/span[2]'
    PASSWORD_FAQ = 'Пароль должен содержать минимум 8 символов, буквы в нижнем и верхнем регистре, цифры и специальные символы'
    CHECKBOX = '//*[@id="password-user"]/div/div[1]/div/div/div[4]/label'
    REGISTER_BUTTON = '//*[@id="RegisterEnd"]'
    SUCCESS_REGISTRATION_XPATH = '//*[@id="invest-moscow-app"]/div[8]/form/div[1]/div[2]'
    SUCCESS_REGISTRATION = 'Поздравляем! Ваша учетная запись успешно создана на инвестиционном портале. На вашу электронную почту отправлено письмо. Активируйте учетную запись для завершения регистрации.'
    VALIDATION_ERROR_XPATH = '//*[@id="personal-info"]/div[1]/div/div/div[6]/span'
    VALIDATION_ERROR = 'Данный почтовый адрес уже зарегистрирован на портале.'


    def fill_information(self):
        last_name = self.get_visible_by_xpath(self.LAST_NAME_XPATH)
        last_name.send_keys(self.LAST_NAME)
        name = self.get_visible_by_xpath(self.NAME_XPATH)
        name.send_keys(self.NAME)
        middle_name = self.get_visible_by_xpath(self.MIDDLE_NAME_XPATH)
        middle_name.send_keys(self.MIDDLE_NAME)
        position = self.get_visible_by_xpath(self.POSITION_XPATH)
        position.send_keys(self.POSITION)
        phone = self.get_visible_by_xpath(self.PHONE_XPATH)
        phone.send_keys(self.PHONE)
        email = self.get_visible_by_xpath(self.EMAIL_XPATH)
        email.send_keys(self.EMAIL)
        index = self.get_visible_by_xpath(self.INDEX_XPATH)
        index.send_keys(self.INDEX)
        fact_adress = self.get_visible_by_xpath(self.FACT_ADRESS_XPATH)
        fact_adress.send_keys(self.FACT_ADRESS)
        inn = self.get_visible_by_xpath(self.INN_XPATH)
        inn.send_keys(self.INN)

    def fill_organisation(self):
        opf = Select(self.get_visible_by_xpath(self.OPF_XPATH))
        opf.select_by_value(self.OPF)
        org_name = self.get_visible_by_xpath(self.ORG_NAME_XPATH)
        org_name.send_keys(self.ORG_NAME)
        legal_adress = self.get_visible_by_xpath(self.LEGAL_ADRESS_XPATH)
        legal_adress.send_keys(self.LEGAL_ADRESS)

    def fill_password(self):
        password = self.get_visible_by_xpath(self.PASSWORD_XPATH)
        password.send_keys(self.PASSWORD)
        repeat_password = self.get_visible_by_xpath(self.REPEAT_PASSWORD_XPATH)
        repeat_password.send_keys(self.PASSWORD)
        checkbox = self.get_clicable_by_xpath(self.CHECKBOX)
        checkbox.click()
