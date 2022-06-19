from autotests.pages.base_page import BasePage



class UmbracoPage(BasePage):
    PATH = '/Umbraco'
    LOGIN_XPATH = '//*[@id="login"]/div[4]/div/div[1]/form/div[2]/input'
    LOGIN = 'content manager'
    PASSWORD_XPATH = '//*[@id="login"]/div[4]/div/div[1]/form/div[3]/input'
    PASSWORD = 'XzAcz4!4D'
    ENTER_BUTTON = '//*[@id="login"]/div[4]/div/div[1]/form/div[4]/div[1]/button'
    SEARCH_XPATH = '//*[@id="search-field"]'
    SEARCH_RESULT_XPATH = '//*[@id="search-results"]/ul/li/div[2]/ul/li/div/a[1]'
    HEADER_XPATH = '//*[@id="contentcolumn"]/div/div/form/div/div[1]/div/div/div/div[1]/ng-form/input'
    HEADER_XPATH = '//*[text()[contains(.,"test_registration@upt24.ru")]]'
    UMBRACO_NAME = '#name'
    UMBRACO_SURNAME = '//*[@id="surName"]'
    UMBRACO_NAME2 = '//*[@id="contactName"]'
    UMBRACO_MIDDLE_NAME = '//*[@id="contactMiddleName"]'
    UMBRACO_SURNAME2 = '//*[@id="contactSurName"]'
    UMBRACO_POSITION = '//*[@id="position"]'
    UMBRACO_INDEX = '//*[@id="index"]'
    UMBRACO_LEGAL_ADRESS = '//*[@id="jurAddress"]'
    UMBRACO_FACT_ADRESS = '//*[@id="factAddress"]'
    UMBRACO_INN = '//*[@id="inn"]'
    UMBRACO_ORG_NAME = '//*[@id="orgName"]'
    UMBRACO_ORG_FORM = '//*[@id="orgForm"]'
    UMBRACO_PHONE_XPATH = '//*[@id="phone"]'
    UMBRACO_PHONE = '8(945) 456-76-34'
    ACTION_BUTTON = '//*[@id="contentcolumn"]/div/div/form/div/div[1]/div/div/div/div[2]/div/a'
    DELETE_BUTTON = '//*[@id="contentcolumn"]/div/div/form/div/div[1]/div/div/div/div[2]/div/ul/li[1]/a'
    CHECK_ACCOUNT = '//*[@id="old-dialog-service"]/div/div/p/strong'
    ACCEPT_DELETE_BUTTON = '//*[@id="old-dialog-service"]/div/div/div/div/div/a[2]'
    ALL_MEMBERS_XPATH = '//*[@id="contentcolumn"]/div/div/form/div/div[1]/div/div/div/div[1]/div[1]'
    ALL_MEMBERS = 'Все участники'



    def umbraco_authorization(self):
        login = self.get_visible_by_xpath(self.LOGIN_XPATH)
        login.send_keys(self.LOGIN)
        password = self.get_visible_by_xpath(self.PASSWORD_XPATH)
        password.send_keys(self.PASSWORD)
        enter = self.get_clicable_by_xpath(self.ENTER_BUTTON)
        enter.click()