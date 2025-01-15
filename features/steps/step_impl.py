import requests

from behave import *
from utilities.payloads import *
from utilities.configurations import *
from utilities.resources import ApiResources

@given('the Book details which needs to be added to Library')
def step_impl(context):
    base_url = get_config()['API']['endpoint']
    context.headers = ApiResources.headers
    context.add_url = f"{base_url}{ApiResources.add_book}"
    query = 'select * from books'
    context.payload = add_book_payload(query)

@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.add_url, json=context.payload, headers=context.headers)
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
    context.payload = add_book_payload_para(isbn,aisle)

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

@then('status code of response should be {status_code:d}') # Parameters the status_code to be used for all BDDs
def step_impl(context, status_code):
    assert context.response.status_code == status_code
