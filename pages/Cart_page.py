from pages.Base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):

    empty_cart_text = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")
    delete_button = (By.CSS_SELECTOR, '[data-test="cartItem-deleteBtn"]')


    def verify_empty_cart(self, empty_cart_text):
        actual_text = self.find_element(*self.empty_cart_text).text
        assert actual_text == empty_cart_text, f"Your cart text is '{actual_text}' but says '{empty_cart_text}'"


    def verify_cart_quantity(self, number_in_cart):
        cart_number = self.find_elements(*self.delete_button)
        assert len(cart_number) == int(number_in_cart), f"Expected {number_in_cart} items in cart, got {len(cart_number)}"