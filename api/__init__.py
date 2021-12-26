from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .playlists.router import router as playlists_router


api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET'],
    allow_headers=['*']
)

api.include_router(playlists_router)
