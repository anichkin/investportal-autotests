from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from autotests.pages.base_page import BasePage


class ProjectsPage(BasePage):

    PATH = '/about-moscow/projects'
    TITLE = 'Проекты - Инвестиционный портал Москвы'
    PROJECTS = (By.XPATH, '//*[@id="mm-0"]/div[8]/div[2]/div/div/div[1]')


    def get_title(self):
        '''Функция получения тайтла страницы'''

        return self.driver.title 
    
    def check_projects(self):
        '''Функция для проверки проектов на странице'''

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ProjectsPage.PROJECTS))

        
        