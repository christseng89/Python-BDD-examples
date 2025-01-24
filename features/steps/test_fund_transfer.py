from behave import given, when, then, step

# ---------------------------- Background Steps ----------------------------
@given('user has valid credentials to login')
def step_impl_given(context):
    context.user_logged_in = True
    print("User has logged in with valid credentials.")

# ---------------------------- Scenario Steps ----------------------------
@when('user selects the "{account}" as "From" account')
def step_impl_selects_from(context, account):
    context.from_account = account
    print(f"User selected From account: {account}")

@when('user selects the "{account}" as "To" account')
def step_impl_selects_to(context, account):
    context.to_account = account
    print(f"User selected To account: {account}")

@step('user enters the amount to be transferred as "{amount}"')
def step_impl_enter(context, amount):
    context.amount = float(amount)
    print(f"User entered transfer amount: {amount}")

@step('user clicks on confirmation button')
def step_impl_confirm(context):
    context.transfer_confirmed = True
    print("User clicked the confirmation button.")

@step('User session timeout')
def step_impl_timeout(context):
    context.session_timeout = True
    print("User session timed out.")

@step('User account is blocked or closed')
def step_impl_blocked(context):
    context.account_status = "blocked"
    print("User account is blocked or closed.")

@step('user should see the error message as "{message}"')
def step_impl_error(context, message):
    context.error_message = message
    print(f"User sees message: {message}")
    # Validation logic can be added here.

@step('the checking account balance should be "{balance}"')
def step_impl_checking_balance(context, balance):
    print(f"The checking account balance is expected to be: {balance}")
    # Validation logic for checking account balance can be added here.

@step('the savings account balance should be "{balance}"')
def step_impl_saving_balance(context, balance):
    print(f"The savings account balance is expected to be: {balance}")
    # Validation logic for savings account balance can be added here.
