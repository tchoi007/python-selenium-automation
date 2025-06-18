from pages.Base_page import Page
from selenium.webdriver.common.by import By

class Signin(Page):

    signin_text = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")

    def sign_in_text(self, expected_text):
        self.wait_for_element(*self.signin_text)
        self.verify_text(expected_text, *self.signin_text)
