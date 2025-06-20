from pages.Base_page import Page
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



class TermsConditionPage(Page):
    def verify_terms_condition(self):
        self.wait_for_url_contains("terms-conditions")