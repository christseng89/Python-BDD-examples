import requests
import json
from utilities.payloads import *
from utilities.configurations import *
from utilities.resources import ApiResources

# Base URL
# print (f"Endpoint {get_config()['API']['endpoint']}")
base_url = get_config()['API']['endpoint']

try:
    headers = ApiResources.headers
    # 1. Add a Book
    add_url = f"{base_url}{ApiResources.add_book}"
    query = 'select * from books'
    response = requests.post(add_url, json=add_book_payload(query), headers=headers)
    response.raise_for_status()
    add_response = response.json()

    # Print AddBook response
    print(f"AddBook Response status: {response.status_code}")
    print(f"AddBook Response: {json.dumps(add_response, indent=2)}")

    # Validate successful addition
    assert add_response["Msg"] == "successfully added", "Book was not added successfully."
    book_id = add_response["ID"]
    print(f"Step #1 - Book ID: {book_id} added successfully.\n")
    print(f"Msg: {add_response["Msg"]}")

    # 2. Get the Book by ID
    get_url = f"{base_url}{ApiResources.get_book}"
    response = requests.get(get_url, params={"ID": book_id})
    response.raise_for_status()
    get_response = response.json()

    # Validate response contains expected data
    assert "book_name" in get_response[0], "Book not found."

    # Print GetBook response
    print(f"Step #2 - GetBook Response: {json.dumps(get_response, indent=2)}\n")
    print(f"GetBook Response status: {response.status_code}")
    print(f"GetBook Name: {get_response[0]['book_name']}\n")

    # 3. Delete the Book by ID
    delete_url = f"{base_url}{ApiResources.delete_book}"
    delete_payload = delete_book_payload(book_id)

    response = requests.post(delete_url, json=delete_payload, headers=headers)
    response.raise_for_status()
    delete_response = response.json()

    # Print DeleteBook response
    print(f"Step #3 - DeleteBook Response: {json.dumps(delete_response, indent=2)}")
    print(f"DeleteBook Response status: {response.status_code}")
    # Validate successful deletion
    assert delete_response["msg"] == "book is successfully deleted", "Book was not deleted successfully."
    print(f"DeleteBook with ID {book_id} deleted successfully.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error: {http_err}")
except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the server.")
except requests.exceptions.Timeout:
    print("Error: Request timed out.")
except requests.exceptions.RequestException as req_err:
    print(f"Request Exception: {req_err}")
except AssertionError as e:
    print(f"Assertion Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
