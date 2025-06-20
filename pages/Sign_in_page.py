from pages.Base_page import Page
from selenium.webdriver.common.by import By

class Signin(Page):

    signin_text = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")
    terms_conditions_link = (By.CSS_SELECTOR, '[aria-label*="terms & conditions"]')

    def sign_in_text(self, expected_text):
        self.wait_for_element(*self.signin_text)
        self.verify_text(expected_text, *self.signin_text)

    def open_sign_in_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_terms_and_conditions(self):
        self.wait_for_element_click(*self.terms_conditions_link)