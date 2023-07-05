import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_helper import pom
from webdriver_helper.pom import BasePage, LazyElement

# driver provide http interface to control browser
# instantiated object
driver = Chrome()
# dom: document + object + model to control element
# pom: core + object + model

class PageTest(BasePage):
    testarea = LazyElement(By.CSS_SELECTOR,"#APjFqb")

    def inputaction(self):
        self.testarea.send_keys("vv")


if __name__ == '__main__':
    url = 'https://www.google.com/'
    driver.get(url)
    # get the core object
    # use the basepage = driver
    page = PageTest(driver)
    page.inputaction()
    #title = driver.title
    #print(title)
    #input()
    driver.set_window_size(1920, 1080)  # 设置窗口大小 1920*1080
    time.sleep(5)
    #driver.minimize_window()  # 最小化窗口
    #time.sleep(1)
    #driver.maximize_window()  # 最大化窗口
    #driver.fullscreen_window()  # 全屏窗口
    #driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('apple')  # Enter apple in the search box
    #driver.find_element(By.ID, 'nav-search-submit-text').click()  # Click to search
    #driver.find_element(By.ID, 'kw').send_keys('selenium')  # 搜索框输入selenium
    #driver.find_element(By.ID, 'su').click()  # 点击百度一下
    #driver.back()
    #time.sleep(3)
    #driver.forward()
    #driver.quit()  # 退出浏览器
