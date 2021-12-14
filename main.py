import uvicorn
import os
from fastapi import FastAPI, status
from api.routers import playlists
from dotenv import load_dotenv


load_dotenv() # Loads variables from .env file

PORT = int(os.environ.get('PORT')) or 8000


app = FastAPI()
app.include_router(playlists.router)


@app.get('/', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def root() -> dict[str, str]:
    return {'message': 'Hello, World'}


def main():
    uvicorn.run('main:app', port=PORT, reload=True)


if __name__ == '__main__':
    main()
