import requests


def get_playlist_by_place_temperature(city: str, lat: str, long: str):
    response = requests.get('https://api.github.com/users/gddeazevedo', params={})
    return response.json()
