import requests # https://pypi.org/project/requests/

try:
    response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Chris T'})
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

    print(f"Response Encoding: {response.encoding}")
    print(f"Response Headers Type: {type(response.headers)}")
    for k, v in response.headers.items():
        print(f"Headers key: {k}, value: {v}")
    print('\n')

    json_response = response.json()
    print (f"Response: {response}")
    # print (f"Json Response: {json_response}")

    print(f"Json Response type: {type(json_response)}\n")

    for actual_book in json_response:
        print (f"Actual Book: {actual_book}")
    print ('\n')

    found_book = {}
    for actual_book in json_response:
        if actual_book['isbn'] == '123asdfasd':
            found_book = actual_book
            print(f"Found Book Type: {type(found_book)}")
            break

    for k, v in found_book.items():
        print(f"Found Book key: {k}, value: {v}")

    expectedBook = {
        "book_name": "A BDD Guideline",
        "isbn": "123asdfasd",
        "aisle": "2000124"
    }

    assert found_book == expectedBook

except requests.exceptions.ConnectTimeout:
    print("\nError: Connection to the server timed out. Please check the network or server status.")

except requests.exceptions.ReadTimeout:
    print("\nError: Server response timed out. Please try again later.")

except requests.exceptions.ConnectionError:
    print("\nError: Failed to connect to the server. Please check the server URL or network connection.")

except requests.exceptions.Timeout:
    print("\nError: Request timed out. Please try again later.")

except requests.exceptions.HTTPError as http_err:
    print(f"\nHTTP Error occurred: {http_err}")

except requests.exceptions.RequestException as req_err:
    print(f"\nRequest Error: {req_err}")

except ValueError as json_err:
    print(f"\nError decoding JSON response: {json_err}")

except AssertionError as e:
    print(f"\nAssertionError: {e}")

except Exception as e:
    print(f"\nUnexpected Error: {e}")


except AssertionError as e:
    print(f"\nAssertionCompareError: {e}")
