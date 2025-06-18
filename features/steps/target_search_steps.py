from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
# Updated code to include Behave variables

product_text=(By.CSS_SELECTOR,"span.h-text-bs.h-display-flex")

@given('Open target main page')
def open_main(context):
    context.app.Main_page.open_main()

@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search_product(search_word)


@then('Verify search worked for {search_word}')
def verify_search_results(context, search_word):
    context.app.Search_results_page.verify_search_results()


#    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
#    assert search_word in actual_text, f"Error, expected {search_word} not in actual {actual_text}"