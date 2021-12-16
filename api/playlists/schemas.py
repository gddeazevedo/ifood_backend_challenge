from typing import Any
from pydantic import BaseModel


class PlaylistsResponse(BaseModel):
    playlist: dict[str, Any]
