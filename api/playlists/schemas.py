from typing import Any
from pydantic import BaseModel


class PlaylistsResponse(BaseModel):
    playlist: list[Any]


class TemperatureResponse(BaseModel):
    temperature: float
