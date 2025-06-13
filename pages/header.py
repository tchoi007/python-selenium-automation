from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Header(Page):
    search_field = (By.CSS_SELECTOR, "#search")
    search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    cart_locator = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def search_product(self):
        self.input_text('tea',*self.search_field)
        self.click_element(*self.search_button)

        sleep(5)


    def click_cart_btn(self):
        self.click_element(*self.cart_locator)
        sleep(5)
