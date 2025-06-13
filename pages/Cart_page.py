from pages.Base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):

    empty_cart_text = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")

    def verify_empty_cart(self, empty_cart_text):
        actual_text = self.find_element(*self.empty_cart_text).text
        assert actual_text == empty_cart_text, f"Your cart text is '{actual_text}' but says '{empty_cart_text}'"