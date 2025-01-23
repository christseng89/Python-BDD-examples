from behave import given, when, then


# ---------------------------- Background Steps ----------------------------

@given('user has valid credentials to login')
def step_impl(context):
    """
    Implement the step to simulate a valid user login.
    """
    # Example step implementation:
    context.user_logged_in = True
    print("User has logged in with valid credentials.")


# ---------------------------- Scenario Outline 1: Valid Transfers ----------------------------

@when('user clicks on Transfer Funds')
def step_impl(context):
    """
    Implement the step to simulate user clicking on Transfer Funds.
    """
    context.transfer_funds_clicked = True
    print("User clicked on Transfer Funds.")


@when('user selects the "{account}" as "{account_type}" account')
def step_impl(context, account, account_type):
    """
    Implement the step to select From or To account.
    Parameters:
    - account: The account number (e.g., 14787)
    - account_type: "From" or "To" account
    """
    if account_type == "From":
        context.from_account = account
    elif account_type == "To":
        context.to_account = account
    print(f"User selected {account_type} account: {account}")


@when('user enters the amount to be transferred as "{amount}"')
def step_impl(context, amount):
    """
    Implement the step to specify the transfer amount.
    """
    context.amount = float(amount)
    print(f"User entered transfer amount: {amount}")


@when('user clicks on confirmation button')
def step_impl(context):
    """
    Implement the step to simulate user clicking the confirmation button.
    """
    context.transfer_confirmed = True
    print("User clicked the confirmation button.")


@then('user should see the error message as "{message}"')
def step_impl(context, message):
    """
    Implement the step to validate the error or success message displayed.
    """
    context.error_message = message
    print(f"User sees message: {message}")


@then('user clicks on Account Overview to check account balance')
def step_impl(context):
    """
    Implement the step to simulate user navigating to Account Overview.
    """
    print("User navigated to Account Overview.")


@then('the checking account balance should be "{balance}" for "{account}"')
def step_impl(context, balance, account):
    """
    Implement the step to validate the checking account balance for a given account.
    Parameters:
    - balance: Expected account balance (e.g., '$115.50')
    - account: Account number being checked
    """
    print(f"Checking account balance for account {account} should be: {balance}")


@then('the savings account balance should "{balance}" for "{account}"')
def step_impl(context, balance, account):
    """
    Implement the step to validate the savings account balance for a given account.
    Parameters:
    - balance: Expected account balance
    - account: Account number being checked
    """
    print(f"Savings account balance for account {account} should be: {balance}")


@then('the checking account balance should remain the same for "{account}"')
def step_impl(context, account):
    """
    Implement the step to validate that the checking account balance is unchanged (for invalid cases).
    """
    print(f"Checking account balance for account {account} remains unchanged.")


@then('the savings account balance should remain the same for "{account}"')
def step_impl(context, account):
    """
    Implement the step to validate that the savings account balance is unchanged (for invalid cases).
    """
    print(f"Savings account balance for account {account} remains unchanged.")
