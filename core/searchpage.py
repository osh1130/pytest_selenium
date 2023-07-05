from webdriver_helper.pom import BasePage, LazyElement, By, LazyElementList


class SearchPage(BasePage):
    p_title_list = LazyElementList(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div/div/div/div/div/div[2]/div[1]/h2/a/span')
    def get_all_title(self):
        title = []
        for p in self.p_title_list:
            title.append(str(p.text))
        return  title