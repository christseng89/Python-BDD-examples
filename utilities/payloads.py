import uuid
from datetime import datetime

def add_book_payload():
    # Generate unique ISBN using current time and UUID
    ct = datetime.now().strftime("%Y%m%d")  # Current time in 'YYYYMMDD' format
    unique_id = str(uuid.uuid4())[:5]  # Generate a 6-character UUID
    isbn = f"{ct}{unique_id}"  # Combine current time and UUID

    # Input JSON Payload for AddBook
    payload = {
        "name": f"Learn Appium Automation with Java - {unique_id}",
        "isbn": isbn,
        "aisle": "227",
        "author": "John foe"
    }
    return payload

def delete_book_payload(book_id):
    payload = {"ID": book_id}
    return payload