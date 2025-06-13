from pages.Base_page import Page
from selenium.webdriver.common.by import By



class Searchresults(Page):
    searched_text = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self):
        actual_text = self.find_element(*self.searched_text).text
        assert "tea" in actual_text, f"tea is not {actual_text}"
