import time
from behave import given, when, then, step
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from utilities.configurations import *

# ---------------------------- Background Steps ----------------------------
@given('user has valid credentials to login')
def step_impl_given(context):
    time.sleep(2)
    print(
        "Initializing the ParaBank login page..."
    )

    url = get_config()['PARA_BANK']['url']
    user_name = get_config()['PARA_BANK']['user_name']
    user_password = get_config()['PARA_BANK']['user_password']

    context.driver = webdriver.Chrome(service=Service(get_config()['PARA_BANK']['chrome_driver_path']))
    context.wait = WebDriverWait(context.driver, 30)

    # Get url, enter username and password
    context.driver.get(url)
    context.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(user_name)
    context.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(user_password)

    # Login and click
    context.driver.find_element(By.XPATH, "//input[@value='Log In']").click()


# ---------------------------- Scenario Steps ----------------------------
@when("user clicks on Transfer Funds")
def step_transfer_find_navigation(context):
    time.sleep(2)
    transfer_funds_link = context.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='transfer.htm']"))
    )
    transfer_funds_link.click()
    print("Navigated to Transfer Funds page successfully!")

@when('user selects the "{account}" as "From" account')
def step_impl_selects_from(context, account):
    print(f"From account: {account}")
    from_account_dropdown = context.wait.until(EC.presence_of_element_located((By.ID, "fromAccountId")))
    time.sleep(2)
    for option in from_account_dropdown.find_elements(By.TAG_NAME, 'option'):
        if account.strip().lower() in option.text.strip().lower():
            option.click()
            break

@step('user selects the "{account}" as "To" account')
def step_impl_selects_to(context, account):
    print(f"To account: {account}")
    to_account_dropdown = context.wait.until(EC.presence_of_element_located((By.ID, "toAccountId")))
    time.sleep(2)
    for option in to_account_dropdown.find_elements(By.TAG_NAME, 'option'):
        if account.strip().lower() in option.text.strip().lower():
            option.click()
            break

@step('user enters the amount to be transferred as "{amount}"')
def step_impl_enter_amount(context, amount):
    print(f"Transfer Amount: {amount}")
    time.sleep(2)
    transfer_amount = int(amount.strip())
    context.wait.until(EC.presence_of_element_located((By.ID, "amount"))).send_keys(transfer_amount)

@step('user clicks on confirmation button')
def step_impl_confirm(context):
    print ('Confirm button clicked')
    time.sleep(2)
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Transfer']"))).click()

@then('user should see the message as "{message}"')
def step_impl_error(context, message):
    print(f"Expected Message: {message}")
    time.sleep(2)
    verification_element = context.wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//h1[contains(normalize-space(),{message})]"))
    )

    verification_message = verification_element.text.strip()
    expected_message = message.strip().strip('"')

    # Assertion to compare the messages
    assert expected_message == verification_message, f"Expected '{expected_message}', but got '{verification_message}'"
    print(f"Actual Message: {verification_message}")

@step("user clicks on Account Overview to check account balance")
def step_navigate_account_overview(context):
    # Click and navigate to Account Overview page
    time.sleep(2)
    context.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Accounts Overview"))).click()

@step('FROM account balance should be "{fromBalance} for "{fromAccount}"')
def step_verify_checking_balance(context, from_balance, from_account):
    time.sleep(2)
    balance = context.wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[contains(a,'" + from_account + "')]/following-sibling::td[1]"))).text
    assert balance == from_balance.strip('"'), f"Assertion failed: balance '{balance}' != FromBalance '{from_balance}'"

@step('TO account balance should "{ToBalance} for "{ToAccount}"')
def step_verify_saving_balance(context, to_balance, to_account):
    time.sleep(2)
    balance = context.wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[contains(a,'" + to_account + "')]/following-sibling::td[1]"))).text
    assert balance == to_balance.strip().replace('"', ''), f"Assertion failed: balance '{balance}' != ToBalance '{to_balance}'"

@step('User session timeout')
def step_impl_timeout(context):
    context.session_timeout = True
    print("User session timed out.")

@step('User account is blocked or closed')
def step_impl_blocked(context):
    context.account_status = "blocked"
    print("User account is blocked or closed.")
