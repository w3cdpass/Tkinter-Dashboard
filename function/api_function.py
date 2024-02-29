import requests


def call():
    data_response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    json_data = data_response.json()
    one_time_joke = json_data['joke']
    return one_time_joke

