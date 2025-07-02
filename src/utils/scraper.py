import requests

def simple_get(url):
    response = requests.get(url)
    if response.status_code == 200:
        if response.headers.get('Content-Type') == 'application/json':
            return response.json()
        else:
            return response.text  # Return the raw response content
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")