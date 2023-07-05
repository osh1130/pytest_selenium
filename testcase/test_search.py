import allure
import pytest as pytest


from core.indexpage import IndexPage
from readdata import read_excel

@pytest.mark.parametrize(('keyword','count'), read_excel('E:\SeleniumTesting\datas\ddt.xlsx'))
def test_web_search(driver,keyword, count):
    #conftest to start before test_web_search
    #driver = get_webdriver('chrome')

    #in index core to get the url
    #url = 'https://www.amazon.com.au/'
    #driver.get(url)
    #index_page = IndexPage(driver)

    #visit the test core
    index_page = IndexPage.start(driver)
    #operate the test steps
    search_page = index_page.search(keyword)
    #get result and assert
    titles = search_page.get_all_title()
    #print(len(titles))

    allure.attach(driver.get_screenshot_as_png(),"screenshot")
    assert count == len(titles),len(titles)