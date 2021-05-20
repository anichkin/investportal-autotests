from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PressCentrPage:

    URL = 'https://investmoscow.upt24.ru/press-center'
    TITLE = 'Пресс-центр - Инвестиционный портал Москвы'
    NEWS_AND_EVENTS = (By.XPATH, '//*[@id="invest-moscow-app"]/div[7]/h2')
    INVEST_DAYDJEST = (By.XPATH, '//*[@id="invest-moscow-app"]/div[8]/div[1]/h1')
    
    
    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver


    def get_title(self):
        '''Функция получения тайтла страницы'''
        
        return self.driver.title 

 

    def check_news_and_events(self):
        """Проверка отображения блока новости и мероприятия"""

        news = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PressCentrPage.NEWS_AND_EVENTS))
        

        return news.text


    def check_invest_daydjest(self):
        """Проверка отображения инвестиционного дайджеста"""

        daydjest = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PressCentrPage.INVEST_DAYDJEST))

        return daydjest.text


    

    