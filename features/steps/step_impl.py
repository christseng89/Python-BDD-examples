import requests
import json

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
    # context.response = response.json()
    # context.book_id = response.json()["ID"]

@then('book is successfully added')
def step_impl(context):
    context.book_id = context.response.json()["ID"]
    assert context.response.json()['Msg'] == 'successfully added'
    assert context.response.status_code == 200
