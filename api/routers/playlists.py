from typing import Optional
from fastapi import APIRouter, status
from ..schemas.res import FindPlacesResponse
from ..controllers import playlists_controller


router = APIRouter(
    tags=['Playlists'],
    prefix='/playlists'
)


@router.get('', status_code=status.HTTP_200_OK, response_model=FindPlacesResponse)
def get_playlist_by_place_temperature(
    city: Optional[str] = '',
    lat: Optional[str] = '',
    long: Optional[str] = ''
):
    return playlists_controller.get_playlist_by_place(city, lat, long)
