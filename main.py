import uvicorn
import os
from dotenv import load_dotenv


load_dotenv() # Loads variables from .env file

PORT = int(os.environ.get('PORT')) or 8000

def main():
    uvicorn.run('main:app', port=PORT, reload=True)


if __name__ == '__main__':
    main()
