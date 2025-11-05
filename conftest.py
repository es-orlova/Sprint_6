import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(scope='function')
def driver():
    service = FirefoxService()
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()