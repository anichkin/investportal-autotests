from .base_page import BasePage


class LogoutPage(BasePage):

    PATH = '/umbraco/surface/account/logout'


    def logout_from_page(driver, base_url):
        page = LogoutPage(driver, base_url)
        page.get()
        return page