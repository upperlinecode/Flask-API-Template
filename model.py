import requests

def getImageUrlFrom(query, your_key):
    print(your_key)
    endpoint = f'https://api.giphy.com/v1/gifs/search?api_key={your_key}&q={query}&limit=25&offset=0&rating=G&lang=en'
    print(endpoint)
    response = requests.get(endpoint).json()
    print(response['data'][0]['images']['fixed_height']['url'])
    the_url = response['data'][0]['images']['fixed_height']['url']
    return the_url