import requests
import json
from utilities.configurations import *

url = 'https://api.github.com/user'
github_token = get_config()['API']['github_token']
headers = {
    'Authorization': f'Bearer {github_token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

### Session
se = requests.session()
se.headers = headers

try:
    # GitHub Authentication
    url = "https://api.github.com"
    response = se.get(url)
    print(json.dumps(response.json(), indent=2))
    print(f"{url} Status code: {response.status_code}")
    print('*************************\n')

    # GitHub Get User/Repos
    url2 = url + "/user/repos"
    response = se.get(url2)
    # print(json.dumps(response.json(), indent=2))
    print(f"{url2} Status code: {response.status_code}")
    print('*************************\n')

    # GitHub Get Rate Limit
    url2 = url + "/rate_limit"
    response = se.get(url2)
    print(json.dumps(response.json()['rate'], indent=2))
    print(f"{url2} Status code: {response.status_code}")
    print('*************************\n')

    # GitHub User email
    url2 = url + "/user/followers"
    response = se.get(url2)
    print(json.dumps(response.json()[0]['login'], indent=2))
    print(f"{url2} Status code: {response.status_code}")
    print('*************************\n')

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
