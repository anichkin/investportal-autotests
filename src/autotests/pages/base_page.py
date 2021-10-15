class BasePage:

    PATH=''

    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url + self.__class__.PATH
    
    def get(self):
        self.driver.get(self.url)
