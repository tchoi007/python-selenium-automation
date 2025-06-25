from pages.Base_page import Page
from selenium.webdriver.common.by import By

class Signin(Page):

    signin_text = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")
    terms_conditions_link = (By.CSS_SELECTOR, '[aria-label*="terms & conditions"]')
    email_field = (By.CSS_SELECTOR, '[id="username"]')
    click_continue = (By.CSS_SELECTOR, '[id="login"]')
    password_field = (By.CSS_SELECTOR, '[id="password"]')
    incorrect_pw_text =(By.CSS_SELECTOR, '[id="password--ErrorMessage"]')


    def sign_in_text(self, expected_text):
        self.wait_for_element(*self.signin_text)
        self.verify_text(expected_text, *self.signin_text)

    def open_sign_in_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_terms_and_conditions(self):
        self.wait_for_element_click(*self.terms_conditions_link)


    def enter_email(self):
        email = "kpenvy@gmail.com"
        self.driver.find_element(*self.email_field).send_keys(email)


    def click_continue_btn(self):
        self.driver.find_element(*self.click_continue).click()


    def enter_password_field(self):
        password = "1234567"
        self.driver.find_element(*self.password_field).send_keys(password)

    def verify_incorrect_password(self, expected_text):
        self.wait_for_element(*self.incorrect_pw_text)
        self.verify_text(expected_text, *self.incorrect_pw_text)

