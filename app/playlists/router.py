from typing import Optional, Any
from fastapi import APIRouter, status
from .schemas import PlaylistsResponse, TemperatureResponse
from . import controller


router = APIRouter(
    tags=['Playlists'],
    prefix='/playlists'
)


@router.get('/', status_code=status.HTTP_200_OK)
def get_playlist_by_place_temperature(
    city: Optional[str] = '',
    lat: Optional[str] = '',
    lon: Optional[str] = ''
):
    return controller.get_playlist_by_place_temperature(city, lat, lon)


@router.get('/temperature', status_code=status.HTTP_200_OK, response_model=TemperatureResponse)
def get_place_temperature(
    city: Optional[str] = '',
    lat: Optional[str] = '',
    lon: Optional[str] = ''
):
    return controller.get_place_temperature(city, lat, lon)
