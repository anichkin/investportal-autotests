import pytest
from selenium import webdriver
from autotests.pages.PressCentrPage import PressCentrPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)



def test_news(driver):

    driver.get(PressCentrPage.URL)
    press_centr = PressCentrPage(driver)
    assert press_centr.check_news_and_events() == 'НОВОСТИ И МЕРОПРИЯТИЯ'
    assert press_centr.check_invest_daydjest() == 'ИНВЕСТИЦИОННЫЙ ДАЙДЖЕСТ'





if __name__ == "__main__":

    pytest.main()