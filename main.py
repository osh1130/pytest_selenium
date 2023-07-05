import os
import time

import pytest
from webdriver_helper import get_webdriver
from core.indexpage import IndexPage

#river = get_webdriver('chrome')
#url = 'https://www.amazon.com.au/'
#driver.get(url)

#driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys('apple')
#driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
#goods = driver.find_elements(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div/div/div/div/div/div[2]/div[1]/h2/a/span')
#for good in goods:
#    print(good.text)
#input()
#time.sleep(5)

#index_page = IndexPage(driver)
#search_page = index_page.search('apple')
#titles = search_page.get_all_title()
#print(len(titles))
#for t in titles:
#    print(t)
#    assert "Apple" in t,t
#time.sleep(20)

if __name__ == '__main__':
    pytest.main()
    time.sleep(30)
    os.system("allure generate  ./temps -o reports --clean")


