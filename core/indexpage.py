from webdriver_helper.pom import BasePage, LazyElement, By

from core.searchpage import SearchPage


class IndexPage(BasePage):
    """home core"""
    url = 'https://www.amazon.com.au/'

    # attribute：represent element located
    ipt_search = LazyElement(By.XPATH,'//*[@id="twotabsearchtextbox"]')
    btn_search = LazyElement(By.XPATH,'//*[@id="nav-search-submit-button"]')

    # function：operation
    def search(self,content):
        # use object to call attribute
        self.ipt_search.send_keys(content)
        self.btn_search.click()
        return SearchPage(self.driver)
