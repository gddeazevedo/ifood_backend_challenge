from pydantic import BaseModel


class FindPlacesResponse(BaseModel):
    playlist: list[str]
