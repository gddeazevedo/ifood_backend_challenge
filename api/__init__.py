from fastapi import FastAPI
import playlists


api = FastAPI()

api.include_router(playlists.router)
