import uuid
from datetime import datetime

from utilities.configurations import get_query

def add_book_payload_para(isbn, aisle):
    unique_id = str(uuid.uuid4())[:5]  # Generate a 6-character UUID
    payload = {
        "name": f"Learn Appium Automation with Java - {unique_id}",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }
    return payload

def add_book_payload(query):
    payload = build_book_payload_from_db(query)
    print (f"Payload: {payload}")
    return payload

## Get the first row data from books table in MySQL
def build_book_payload_from_db(query):
    first_row = get_query(query)
    ct = datetime.now().strftime("%Y%m%d")  # Current time in 'YYYYMMDD' format
    unique_id = str(uuid.uuid4())[:5]  # Generate a 6-character UUID
    isbn = f"{ct}{unique_id}"  # Combine current time and UUID

    add_body = {'name': first_row[0], 'isbn': isbn, 'aisle': first_row[2], 'author': first_row[3]}
    print (f"Build first book's body: {add_body}")
    return add_body

def delete_book_payload(book_id):
    payload = {"ID": book_id}
    return payload
