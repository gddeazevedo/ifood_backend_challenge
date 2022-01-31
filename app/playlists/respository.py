import os
import requests


SPOTIFY_API_URL = f"{os.environ.get('SPOTIFY_API_URL')}/{os.environ.get('SPOTIFY_USER_ID')}/playlists"


class OpenWeatherApiRepository:
    @staticmethod
    def get(city: str, lat: str, lon: str):
        params = {
            'appid': os.environ.get('OPEN_WEATHER_MAPS_API_KEY'),
            'q': city,
            'lat': lat,
            'lon': lon,
            'units': 'metric'
        }

        return requests.get(os.environ.get('OPEN_WEATHER_MAPS_API_URL'), params=params)


class SpotifyApiRepository:
    @staticmethod
    def get(temperature: float):
        headers = {
            'Content-Type': 'application/json',
        }

        if temperature > 30:
            # TODO: Fetch party tracks
            pass
        elif 15 <= temperature <= 30:
            # TODO: Fetch pop tracks
            pass
        elif 10 <= temperature <= 14:
            # TODO: Fetch rock music tracks
            pass
        else:
            # TODO: Fetch classical music tracks
            pass

        return requests.get(SPOTIFY_API_URL, headers=headers)
