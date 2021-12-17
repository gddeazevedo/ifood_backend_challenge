from typing import Optional, Any
from fastapi import APIRouter, status
from .schemas import PlaylistsResponse
from api.playlists import controller


router = APIRouter(
    tags=['Playlists'],
    prefix='/playlists'
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=PlaylistsResponse)
def get_playlist_by_place_temperature(
    city: Optional[str] = '',
    lat: Optional[str] = '',
    lon: Optional[str] = ''
):
    return controller.get_playlist_by_place_temperature(city, lat, lon)
