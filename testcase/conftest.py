import pytest
from webdriver_helper import get_webdriver

@pytest.fixture(scope="module")
def driver():
    driver = get_webdriver('chrome')
    yield driver
    #driver.quit()