from fastapi.exceptions import HTTPException
from .respository import OpenWeatherApiRepository, SpotifyApiRepository


def get_place_temperature(city: str, lat: str, lon: str):
    response = OpenWeatherApiRepository.get(city, lat, lon)

    if not response.ok:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.reason)

    data = {
        'temperature': response.json()['main']['temp']
    }

    return data


def get_playlist_by_place_temperature(city: str, lat: str, lon: str):
    data = get_place_temperature(city, lat, lon)

    response = SpotifyApiRepository.get(data['temperature'])

    return response.json()
