from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



# init driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# open the url
driver.get('https://www.target.com/')

#practice
#amazon logo
#driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
#email field
#driver.find_element(By.ID,'ap_email')
#continue button
#driver.find_element(By.ID,'continue')
#conditions
#driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
#privacy notice
#driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
#need help
#driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
#create your account
#driver.find_element(By.ID,"createAccountSubmit")

#action

driver.find_element(By.XPATH,"//span[text()='Account']").click()
sleep(5)
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

sleep(5)
#assertion
expected_text = "Sign in or create account"
actual_text = driver.find_element(By.XPATH,"//h1[text()='Sign in or create account']").text
assert expected_text in actual_text,f"Error, expected {expected_text}, not in actual {actual_text}"
print('test passed')
driver.quit()