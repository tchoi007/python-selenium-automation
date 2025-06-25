from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from pages.Base_page import Page


class TargetHelpPage(Page):
    headers_text = (By.XPATH, '//h1[text()=" {header_text}"]')
    dd_locator = (By.CSS_SELECTOR, '[name*= "ViewHelpTopics"]')


    def open_help(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def _get_header_text(self, expected_text):
        return [self.headers_text[0], self.headers_text[1].replace('{header_text}', expected_text)]

    def verify_header_text(self, expected_text):
        locators = self._get_header_text(expected_text)
        self.wait_for_element(*locators)

    def select_dd(self, value):
        dd = self.find_element(*self.dd_locator)
        select = Select(dd)
        select.select_by_value(value)