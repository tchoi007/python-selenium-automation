from pages.Base_page import Page
from pages.Cart_page import CartPage
from pages.Main_page import MainPage
from pages.Sign_in_page import Signin
from pages.header import Header
from pages.Search_results_page import Searchresults


class Application:
    def __init__(self, driver):
        self.Base_page = Page(driver)
        self.Main_page = MainPage(driver)
        self.header = Header(driver)
        self.Search_results_page = Searchresults(driver)
        self.Cart_page = CartPage(driver)
        self.Sign_in_page = Signin(driver)