import requests
import json

from utilities.payloads import *
from utilities.configurations import *
from utilities.resources import ApiResources

def after_scenario(context, scenario):
    base_url = get_config()['API']['endpoint']
    delete_url = f"{base_url}{ApiResources.delete_book}"
    delete_payload = delete_book_payload(context.book_id)

    response = requests.post(delete_url, json=delete_payload, headers=context.headers)
    delete_response = response.json()

    # Validate successful deletion
    print(f'\tAfter scenario - Book ID: {context.book_id} was deleted!!')
    assert delete_response["msg"] == "book is successfully deleted", "Book was not deleted successfully."
    assert response.status_code == 200
