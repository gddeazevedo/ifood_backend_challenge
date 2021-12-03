import uvicorn
from fastapi import FastAPI, status


app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK, response_model=dict[str, str])
def root() -> dict[str, str]:
    return {'message': 'Hello, World'}


def main():
    uvicorn.run('main:app', port=8000, reload=True)


if __name__ == '__main__':
    main()
