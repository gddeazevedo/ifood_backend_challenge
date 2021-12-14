from typing import Optional, Any
from fastapi import APIRouter, status
from ..schemas.res import PlaylistsResponse
from ..controllers import playlists_controller


router = APIRouter(
    tags=['Playlists'],
    prefix='/playlists'
)


@router.get('', status_code=status.HTTP_200_OK, response_model=PlaylistsResponse)
def get_playlist_by_place_temperature(
    city: Optional[str] = '',
    lat: Optional[str] = '',
    long: Optional[str] = ''
):
    return playlists_controller.get_playlist_by_place_temperature(city, lat, long)
