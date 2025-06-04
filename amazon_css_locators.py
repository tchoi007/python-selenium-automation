from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#Amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

#Create account Text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")


#Your name
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")


#Email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#Password field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

#password must be 6 characters
driver.find_element(By.CSS_SELECTOR, "[id*=ap_password_context]")

#reenter password field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")


#continue button
driver.find_element(By.CSS_SELECTOR, "#continue")

#conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_register_notification_condition_of_use']")



#privacy notice
driver.find_element(By.CSS_SELECTOR, "[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy']")


#already a customer sign in button

driver.find_element(By.CSS_SELECTOR, "#ra-sign-in-link")