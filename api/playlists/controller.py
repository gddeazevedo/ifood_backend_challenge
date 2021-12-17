from fastapi.exceptions import HTTPException
from .respository import SpotifyRepository, OpenWeatherRepository


def get_place_temperature(city: str, lat: str, lon: str):
    response = OpenWeatherRepository.get(city, lat, lon)

    if not response.ok:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.reason)


def get_playlist_by_place_temperature(city: str, lat: str, lon: str):
    response = get_place_temperature(city, lat, lon)

    if not response.ok:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.reason)

    temperature = response.json()['main']['temp']

    response = SpotifyRepository.get(temperature)

    return response.json()
