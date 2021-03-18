from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectsPage:

    URL = 'https://investmoscow.ru/about-moscow/projects'
    TITLE = 'Проекты - Инвестиционный портал Москвы'
    PROJECTS = (By.XPATH, '//*[@id="mm-0"]/div[7]/div[1]/h2')


    def __init__(self, driver):
        '''Вызывается при создании PageObject'''

        self.driver = driver


    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title 
    
    def check_projects(self):
        '''Функция для проверки проектов на странице'''

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProjectsPage.PROJECTS))

        
        