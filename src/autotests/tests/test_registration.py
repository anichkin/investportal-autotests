from autotests.pages.PortalPages.RegistrationPage import RegistrationPage
from autotests.pages.PortalPages.UmbracoPage import UmbracoPage
import allure
import time

def test_registration(driver, base_url):
    """Проверка регистрации Юридического лица"""
    with allure.step('1.Переход на страницу регистрации, выбор типа Лица'):
        page = RegistrationPage(driver, base_url)
        page.get()
        ul = page.get_clicable_by_xpath(page.UL_XPATH)
        assert ul.text == page.UL
        ul.click()
        next1 = page.get_clicable_by_xpath(page.NEXT1_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Переход на вкладку Персональные данные, заполнение её'):
        next1.click()
        page.fill_information()
        next2 = page.get_clicable_by_xpath(page.NEXT2_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('3. Переход на вкладку Информация об организации, её заполнение'):
        next2.click()
        page.fill_organisation()
        next3 = page.get_clicable_by_xpath(page.NEXT3_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('4. Переход на вкладку Установка пароля, заполнение'):
        next3.click()
        page.fill_password()
        assert page.get_visible_by_xpath(page.PASSWORD_FAQ_XPATH).text == page.PASSWORD_FAQ
        register = page.get_clicable_by_xpath(page.REGISTER_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('5. Переход на завершение регистрации'):
        register.click()
        try:
            success = page.get_visible_by_xpath_long(page.SUCCESS_REGISTRATION_XPATH)
            assert success.text == page.SUCCESS_REGISTRATION
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        except Exception:
            validation_error = page.get_visible_by_xpath_long(page.VALIDATION_ERROR_XPATH)
            assert validation_error.text == page.VALIDATION_ERROR
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot")


def test_delete_account(driver, base_url):
    """Удаление созданного аккаунта из умбраки"""
    with allure.step('1. Вход в умбраку'):
        page = UmbracoPage(driver, base_url)
        page.get()
        page.umbraco_authorization()
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('2. Поиск аккаунта в умбраке'):
        search = page.get_visible_by_xpath_long(page.SEARCH_XPATH)
        search.send_keys(RegistrationPage.EMAIL)
        search_result = page.get_visible_by_xpath_long(page.SEARCH_RESULT_XPATH)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
    with allure.step('3. Переход в запись об аккаунте и удаление аккаунта'):
        search_result.click()
        page.umbraco_authorization()
        action = page.get_clicable_by_xpath(page.ACTION_BUTTON)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        action.click()
        delete = page.get_clicable_by_xpath(page.DELETE_BUTTON)
        delete.click()
        check = page.get_visible_by_xpath_long(page.CHECK_ACCOUNT)
        assert check.text == RegistrationPage.EMAIL
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")
        accept_delete = page.get_clicable_by_xpath(page.ACCEPT_DELETE_BUTTON)
        accept_delete.click()
        all_members = page.get_visible_by_xpath_long(page.ALL_MEMBERS_XPATH)
        assert all_members.text == page.ALL_MEMBERS
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot")




        # assert header.text == RegistrationPage.EMAIL
        # umbraco_name = page.get_visible_by_xpath(page.UMBRACO_NAME)
        # assert umbraco_name.text == RegistrationPage.NAME
        # umbraco_surname = page.get_visible_by_xpath(page.UMBRACO_SURNAME)
        # assert umbraco_surname.text == RegistrationPage.LAST_NAME
        # umbraco_name2 = page.get_visible_by_xpath(page.UMBRACO_SURNAME2)
        # assert umbraco_name2.text == RegistrationPage.NAME
        # umbraco_middle_name = page.get_visible_by_xpath(page.UMBRACO_MIDDLE_NAME)
        # assert umbraco_middle_name.text == RegistrationPage.MIDDLE_NAME
        # umbraco_surname2 = page.get_visible_by_xpath(page.UMBRACO_SURNAME2)
        # assert umbraco_surname2.text == RegistrationPage.LAST_NAME
        # umbraco_position = page.get_visible_by_xpath(page.UMBRACO_POSITION)
        # assert umbraco_position.text == RegistrationPage.POSITION
        # umbraco_index = page.get_visible_by_xpath(page.UMBRACO_INDEX)
        # assert umbraco_index.text == RegistrationPage.INDEX
        # umbraco_legal_adress = page.get_visible_by_xpath(page.UMBRACO_LEGAL_ADRESS)
        # assert umbraco_legal_adress.text == RegistrationPage.LEGAL_ADRESS
        # umbraco_fact_adress = page.get_visible_by_xpath(page.UMBRACO_FACT_ADRESS)
        # assert umbraco_fact_adress.text == RegistrationPage.FACT_ADRESS
        # umbraco_inn = page.get_visible_by_xpath(page.UMBRACO_INN)
        # assert umbraco_inn.text == RegistrationPage.INN
        # umbraco_org_name = page.get_visible_by_xpath(page.UMBRACO_ORG_NAME)
        # assert umbraco_org_name.text ==RegistrationPage.ORG_NAME
        # umbraco_org_form = page.get_visible_by_xpath(page.UMBRACO_ORG_FORM)
        # assert umbraco_org_form.text == RegistrationPage.OPF
        # umbraco_phone = page.get_visible_by_xpath(page.UMBRACO_PHONE_XPATH)
        # assert umbraco_phone.text == page.UMBRACO_PHONE