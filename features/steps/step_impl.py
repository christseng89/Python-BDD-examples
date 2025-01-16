import requests
import csv
import os

from behave import *
from utilities.payloads import *
from utilities.configurations import *
from utilities.resources import ApiResources

# Book Demo


@given('the Book details which needs to be added to Library')
def step_impl(context):
    base_url = get_config()['API']['endpoint']
    context.headers = ApiResources.headers
    context.add_url = f"{base_url}{ApiResources.add_book}"
    query = 'select * from books'
    context.payload = add_book_payload(query)


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(
        context.add_url, json=context.payload, headers=context.headers)
    context.book_id = context.response.json()["ID"]


@then('book is successfully added')
def step_impl(context):
    assert context.response.json()['Msg'] == 'successfully added'
    assert context.response.status_code == 200


@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    base_url = get_config()['API']['endpoint']
    context.headers = ApiResources.headers
    context.add_url = f"{base_url}{ApiResources.add_book}"
    context.payload = add_book_payload_para(isbn, aisle)

# GitHub Demo


@given('I have GitHub token')
def step_impl(context):
    context.github_token = get_config()['API']['github_token']
    headers = {
        'Authorization': f'Bearer {context.github_token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    context.se = requests.session()
    context.se.headers = headers
    context.url = ApiResources.github_user_repos


@when('I hit getRepo API of GitHub')
def step_impl(context):
    context.response = context.se.get(context.url)


# Parameters the status_code to be used for all BDDs
@then('status code of response should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code

# Loan Application


@given('the file path exists {file_path}')
def step_given_file_path_exists(context, file_path):
    """Set the file path and validate existence."""
    context.file_path = file_path
    context.file_exists = os.path.exists(context.file_path)

    if context.file_exists:
        try:
            with open(context.file_path, 'r') as file:
                # Convert to list for subscriptable access
                context.file_content = list(csv.reader(file))
        except Exception as e:
            context.file_content = None
            context.file_error = str(e)
    else:
        context.file_content = None
        context.file_error = "File does not exist."

    assert context.file_content is not None, f"Error: {context.file_error}"


@when('I read the file')
def step_when_read_file(context):
    """Read the file and extract names, amounts, and status arrays."""
    context.names = []
    context.amounts = []
    context.status = []

    # Skip the header and process data rows
    for row in context.file_content[1:]:
        if len(row) >= 3:  # Ensure row has enough columns
            context.names.append(row[0])
            context.amounts.append(row[1])
            context.status.append(row[2])

    assert len(context.names) > 0, "No valid data rows found in the file."


@then('{name} in records')
def step_then_see_arrays(context, name):
    """Verify Name in records."""
    if name in context.names:
        index = context.names.index(name)
    else:
        index = None

    assert index is not None, f"{name} was not found!"
