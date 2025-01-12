import requests
import json

url = "https://httpbin.org/cookies"
cookies = {"visit-year": "2025"}
timeout = 3

se = requests.session()
se.cookies.update(cookies)
headers = {
    'accept': 'application/json'
}
pet_id = 123456

try:
    res = se.get(url, cookies={"visit-month": "Jan"})
    print (f"{url} Response cookies: {json.dumps(res.json(), indent=2)}")
    print (f"{url} Response history: {res.history}, status code: {res.status_code}")
    print ('\n')

    url2 = url + "/delete?visit-month=Jan"
    res = se.get(url2)
    print (f"{url2} Response cookies: {json.dumps(res.json(), indent=2)}")
    print (f"{url} Response history: {res.history}, status code: {res.status_code}")
    print ('\n')

    # Upload multiple files https://requests.readthedocs.io/en/latest/user/advanced/#post-multiple-multipart-encoded-files
    url = 'https://httpbin.org/post'
    files = {'file': open('test.txt', 'rb')}
    res = requests.post(url, files=files)
    print (f"{url} Response json: {json.dumps(res.json()['files'], indent=2)}, status code {res.status_code}")
    print('************\n')

    # Redirection
    url = 'http://rahulshettyacademy.com'
    res = requests.get(url, cookies=cookies)
    # print (f"{url} Response text: {res.text}")
    print (f"{url} Response status code: {res.status_code}, redirect: {res.is_redirect}, history: {res.history}")

    res = requests.get(url, cookies=cookies, allow_redirects=False)
    # print (f"{url} Response text: {res.text}")
    print (f"{url} Response status code: {res.status_code}, redirect: {res.is_redirect}, history: {res.history}")

    # Timeout after ? secs https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
    res = requests.get(url, cookies=cookies, allow_redirects=False, timeout=timeout) # 0.01 => timeout error
    # print (f"{url} Response text: {res.text}")
    print (f"{url} Response status code: {res.status_code}, redirect: {res.is_redirect}, history: {res.history}, timeout: {timeout}")
    print('************\n')

    # https://petstore.swagger.io/#/pet/uploadFile
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}/uploadImage"
    files=[
      ('file',(open('test.txt','rb')))
    ]
    res = requests.request("POST", url, headers=headers, files=files)
    print(f"{url} Response json: {json.dumps(res.json(), indent=2)}, status code {res.status_code}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error for {url}: {http_err}")
except requests.exceptions.Timeout:
    print(f"Error: Request to {url} timed out.")
except requests.exceptions.ConnectionError:
    print(f"Error: Unable to connect to {url}.")
except requests.exceptions.RequestException as req_err:
    print(f"Request Exception for {url}: {req_err}")
except Exception as err:
    print(f"Unexpected Error for {url}: {err}")