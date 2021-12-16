import os
import requests
from fastapi.exceptions import HTTPException


SPOTIFY_API_URL = f"{os.environ.get('SPOTIFY_API_URL')}/{os.environ.get('SPOTIFY_USER_ID')}/playlists"


def get_playlist_by_place_temperature(city: str, lat: str, lon: str):
    params = {
        'appid': os.environ.get('OPEN_WEATHER_MAPS_API_KEY'),
        'q': city,
        'lat': lat,
        'lon': lon,
        'units': 'metric'
    }

    response = requests.get(os.environ.get('OPEN_WEATHER_MAPS_API_URL'), params=params)

    if not response.ok:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.reason)

    temperature = response.json()['main']['temp']

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(SPOTIFY_API_URL, headers=headers)

    if not response.ok:
        print(response.url)
        raise HTTPException(
            status_code=response.status_code,
            detail=response.reason)

    if temperature > 30:
        # TODO: Fetch party tracks
        pass
    elif temperature >= 15 and temperature <= 30:
        # TODO: Fetch pop tracks
        pass
    elif temperature >= 10 and temperature <= 14:
        # TODO: Fetch rock music tracks
        pass
    else:
        # TODO: Fetch classical music tracks
        pass  

    return response.json()
