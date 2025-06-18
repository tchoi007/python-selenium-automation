from pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Searchresults(Page):
    searched_text = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    product_title = (By.CSS_SELECTOR, '[title*="Orange LED Flashlight Orange - Embark"]')
    click_add_cart = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    click_close_popup_locator = (By.CSS_SELECTOR, '[aria-label="close"]')



    def verify_search_results(self):
        actual_text = self.find_element(*self.searched_text).text
        assert "tea" in actual_text, f"tea is not {actual_text}"


    def click_product_title(self):
        self.wait_for_element_click(*self.product_title)
        sleep(3) #Stale element without sleep. Element exists but needs time to load?

    def click_add_to_cart(self):
        self.wait_for_element_click(*self.click_add_cart)


    def click_close_popup(self):
        self.wait_for_element_click(*self.click_close_popup_locator)