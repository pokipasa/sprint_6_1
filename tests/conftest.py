import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.main_url)
    yield driver
    driver.quit()
