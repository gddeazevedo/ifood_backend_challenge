import uvicorn
from fastapi import FastAPI, status
from api.routers import playlists


app = FastAPI()

app.include_router(playlists.router)


@app.get('/', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def root() -> dict[str, str]:
    return {'message': 'Hello, World'}


def main():
    uvicorn.run('main:app', port=8000, reload=True)


if __name__ == '__main__':
    main()
