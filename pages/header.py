from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Header(Page):
    search_field = (By.CSS_SELECTOR, "#search")
    search_button = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    cart_locator = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    account_btn = (By.CSS_SELECTOR, "#account-sign-in")
    sign_in_btn = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search_product(self, search_word):
        self.input_text(search_word,*self.search_field)
        self.click_element(*self.search_button)

        sleep(10) #needed because ad popup, element is underneath


    def click_cart_btn(self):
        self.click_element(*self.cart_locator)
        #sleep(5)

    def click_account_btn(self):
        self.click_element(*self.account_btn)


    def click_sign_in(self):
        self.wait_for_element_click(*self.sign_in_btn)




        # self.wait_for_element(*self.CART_ICON)
        # self.wait_for_element_click(*self.CART_ICON)

        # Stale El Ref Exception
        # element = self.driver.find_element(*self.CART_ICON)
        # print(element)
        # self.driver.refresh()
        # element = self.driver.find_element(*self.CART_ICON)
        # print(element)
        # element.click()