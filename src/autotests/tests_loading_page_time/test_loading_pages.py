from typing import List
import pytest
from selenium import webdriver
from autotests.pages.PortalPages.about_moscow_page import AboutMoscowPage
from autotests.pages.PortalPages.investment_map_page import InvestmentMapPage
from autotests.pages.PortalPages.main_page import MainPage
from autotests.pages.PortalPages.moscow_in_numbers_page import MoscowInNumberPage
from autotests.pages.PortalPages.online_services_page import OnlineServicesPage
from autotests.pages.PortalPages.podpiska_inwest_digest_page import PodpiskaInwestDigestPage
from autotests.pages.PortalPages.projects_page import ProjectsPage
from autotests.pages.PortalPages.tenders_page import TendersPage



TEST_RUN_AMAONT = 10


def assert_loading_page_times(times: List[int], max_time: float, percent: float):
    good = list(filter(lambda time: time/1000 <= max_time, times))
    assert len(good)/len(times) >= percent, \
        f'Too many slow loading: {len(times)-len(good)} from {len(times)}'


@pytest.mark.loading_page_time
@pytest.mark.parametrize(('path', 'max_time', 'percent'),
    [
        (AboutMoscowPage.PATH, 10, 0.95),
        (InvestmentMapPage.PATH, 10, 0.95),
        (MainPage.PATH, 10, 0.95),
        (MoscowInNumberPage.PATH, 10, 0.95),
        (OnlineServicesPage.PATH, 10, 0.95),
        (PodpiskaInwestDigestPage.PATH, 10, 0.95),
        (ProjectsPage.PATH, 10, 0.95),
        (TendersPage.PATH, 10, 0.95), 
    ]
)
def test_loading_pages_without_cache(base_url, path, max_time, percent):
    times = []
    for _ in range(TEST_RUN_AMAONT):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get(base_url+path)
        start = driver.execute_script('return window.performance.timing.navigationStart')
        end = driver.execute_script('return window.performance.timing.loadEventEnd')
        times.append(end-start)
        driver.close()
    print(times)
    assert_loading_page_times(times, max_time, percent)
