import requests
import json
from utilities.configurations import *

url = 'https://api.github.com/user'
github_token = get_config()['API']['github_token']
headers = {
    'Authorization': f'Bearer {github_token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

try:
    url = "https://api.github.com"
    response = requests.request("GET", url, headers=headers)

    print(json.dumps(response.json(), indent=2))

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
