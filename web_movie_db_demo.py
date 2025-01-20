import requests
from utilities.configurations import get_config

try:
    # Get the token from configuration
    token = get_config()['MOVIE_DB']['token']
    base_url = get_config()['MOVIE_DB']['url']

    # Define the URL
    url = base_url + "/tv/top_rated?language=en-US&page=1"

    # Set up headers
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    # Make the API request
    response = requests.get(url, headers=headers)
    # Process the response
    data = response.json()

    # Extract `original_name` from results
    if 'results' in data and isinstance(data['results'], list):
        original_names = [result['original_name'] for result in data['results'] if 'original_name' in result]
        print("\n\tTop Rated TV Series Names:")
        print("\t*******************************")
        for name in original_names:
            print("\t" + name)
    else:
        print("Unexpected response format. No 'results' field found.")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except KeyError as key_err:
    print(f"Configuration error: Missing key - {key_err}")
except Exception as err:
    print(f"An unexpected error occurred: {err}")
