from fastapi import FastAPI
from .playlists.router import router as playlists_router


api = FastAPI()

api.include_router(playlists_router)
