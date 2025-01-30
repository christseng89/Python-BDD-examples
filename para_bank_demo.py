from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from utilities.configurations import *

# Path to the ChromeDriver binary
CHROMEDRIVER_PATH = get_config()['PARA_BANK']['chrome_driver_path']
url = get_config()['PARA_BANK']['url']
user_name = get_config()['PARA_BANK']['user_name']
user_password = get_config()['PARA_BANK']['user_password']

driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH))

# Set up WebDriverWait for the context
wait = WebDriverWait(driver, 20)

print("Driver initialized successfully.")

try:
    # Step 1: Open the ParaBank login page
    driver.get(url)

    # Step 2: Login
    wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(user_name)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(user_password)
    login_button = driver.find_element(By.XPATH, "//input[@value='Log In']")
    login_button.click()
    print("Login successful!")

    # Step 3: Navigate to Transfer Funds page
    driver.find_element(By.XPATH, "//a[@href='transfer.htm']").click()

    # # Step 4: Wait for "fromAccountId" drop-down and its options
    # wait.until(EC.visibility_of_element_located((By.ID, "fromAccountId")))
    # from_account_dropdown = driver.find_element(By.ID, "fromAccountId")
    #
    # # Wait for options to populate
    # all_options = None
    # select = None
    # for i in range(10):  # Retry up to 10 times
    #     select = Select(from_account_dropdown)
    #     all_options = [option.text for option in select.options]
    #     if all_options:  # If options are populated, break the loop
    #         break
    #     # print("Waiting for options to populate...")
    #     time.sleep(1)
    #
    # # Debugging - Print all available options in the drop-down
    # # print(f"Available options in 'From Account' drop-down: {all_options}")
    #
    # account = "14565"
    # # Step 5: Select the account '14565' if it exists
    # if account in all_options:
    #     select.select_by_visible_text(account)
    #     selected_option = select.first_selected_option
    #     print(f"Selected from account: '{selected_option.text}'")
    # else:
    #     print(f"Account '{account}' is not available in the drop-down options.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
