from pydantic import BaseModel


class PlaylistsResponse(BaseModel):
    playlist: list[str]
