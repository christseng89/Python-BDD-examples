import time
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from utilities.configurations import get_config

# ---------------------------- Background Steps ----------------------------
@given('user has valid credentials to login')
def step_impl_given(context):
    print("Initializing the ParaBank login page...")

    url = get_config()['PARA_BANK']['url']
    user_name = get_config()['PARA_BANK']['user_name']
    user_password = get_config()['PARA_BANK']['user_password']

    context.driver = webdriver.Chrome(service=Service(get_config()['PARA_BANK']['chrome_driver_path']))
    context.wait = WebDriverWait(context.driver, 90)

    # Open URL and login
    context.driver.get(url)
    context.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(user_name)
    context.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(user_password)
    context.driver.find_element(By.XPATH, "//input[@value='Log In']").click()

# ---------------------------- Scenario Steps ----------------------------

@when("user clicks on Transfer Funds")
def step_transfer_find_navigation(context):
    transfer_funds_link = context.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'transfer.htm')]"))
    )
    transfer_funds_link.click()
    print("Navigated to Transfer Funds page successfully!")

@when('user selects "{account}" as the "From" account')
def step_impl_selects_from(context, account):
    from_account_dropdown = context.wait.until(EC.presence_of_element_located((By.ID, "fromAccountId")))
    for option in from_account_dropdown.find_elements(By.TAG_NAME, 'option'):
        if option.text.strip() == account.strip():
            option.click()
            break

@when('user selects "{account}" as the "To" account')
def step_impl_selects_to(context, account):
    to_account_dropdown = context.wait.until(EC.presence_of_element_located((By.ID, "toAccountId")))
    for option in to_account_dropdown.find_elements(By.TAG_NAME, 'option'):
        if option.text.strip() == account.strip():
            option.click()
            break

@when('user enters the amount "{amount}" to be transferred')
def step_impl_enter_amount(context, amount):
    transfer_amount = context.wait.until(EC.presence_of_element_located((By.ID, "amount")))
    transfer_amount.clear()
    transfer_amount.send_keys(amount.strip())

@when("user clicks on the confirmation button")
def step_impl_confirm(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Transfer']"))).click()
    print("Transfer initiated.")

@then('user should see the message "{message}"')
def step_impl_error(context, message):
    verification_element = context.wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//h1[contains(text(), '{message}')]"))
    )
    verification_message = verification_element.text.strip()
    assert verification_message == message.strip(), f"Expected '{message}', but got '{verification_message}'"

@when("user clicks on Account Overview to check the account balance")
def step_navigate_account_overview(context):
    context.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Accounts Overview"))).click()

@then('FROM account balance should be "{from_balance}" for "{from_account}"')
def step_verify_from_balance(context, from_balance, from_account):
    balance = context.wait.until(
        EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{from_account}')]/following-sibling::td[1]"))
    ).text.strip()
    assert balance == from_balance, f"Assertion failed: balance '{balance}' != expected '{from_balance}'"

@then('TO account balance should be "{to_balance}" for "{to_account}"')
def step_verify_to_balance(context, to_balance, to_account):
    balance = context.wait.until(
        EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{to_account}')]/following-sibling::td[1]"))
    ).text.strip()
    assert balance == to_balance, f"Assertion failed: balance '{balance}' != expected '{to_balance}'"

@then('User session timeout')
def step_impl_timeout(context):
    context.session_timeout = True
    print("User session timed out.")

@then('User account is blocked or closed')
def step_impl_blocked(context):
    context.account_status = "blocked"
    print("User account is blocked or closed.")
