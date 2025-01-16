import requests
import json
from utilities.configurations import *

url = 'https://api.github.com'
github_token = get_config()['API']['github_token']
headers = {
    'Authorization': f'Bearer {github_token}',
    'X-GitHub-Api-Version': '2022-11-28'
}

# Initialize session
se = requests.session()
se.headers = headers


def fetch_and_process(api_session, endpoint, response_processor=None):
    """Fetch data from the given endpoint and process the response."""
    try:
        response = api_session.get(endpoint)
        print(f"{endpoint} Status code: {response.status_code}")

        # Raise an error for unsuccessful requests
        response.raise_for_status()

        if response_processor:
            # Custom processing for the response
            response_processor(response)
        else:
            # Default processing: pretty-print the JSON response
            print(json.dumps(response.json(), indent=2))

        print('*************************\n')
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error for {endpoint}: {http_err}")
    except requests.exceptions.ConnectionError:
        print(f"Error: Unable to connect to {endpoint}.")
    except requests.exceptions.Timeout:
        print(f"Error: Request to {endpoint} timed out.")
    except requests.exceptions.RequestException as req_err:
        print(f"Request Exception for {endpoint}: {req_err}")
    except Exception as err:
        print(f"Unexpected Error for {endpoint}: {err}")


try:
    # GitHub Authentication
    fetch_and_process(se, url)

    # GitHub Get User Repos
    fetch_and_process(se, f"{url}/user/repos")

    # GitHub Get Rate Limit
    fetch_and_process(se, f"{url}/rate_limit",
                      lambda response: print(json.dumps(response.json().get('rate', {}), indent=2)))

    # GitHub User Followers
    fetch_and_process(se, f"{url}/user/followers",
                      lambda response: print(json.dumps(response.json()[0]['login'], indent=2)))

except Exception as e:
    print(f"Unexpected Error in main execution: {e}")
