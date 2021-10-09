class BasePage:

    PATH=''

    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = self.__class__.PATH + base_url
    
    def get(self):
        self.driver.get(self.url)
