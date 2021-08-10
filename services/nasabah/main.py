import asyncio
from logging import log
import os
import structlog
import asyncpg

from repository import NasabahRepository
from app import NasabahApp
from api import RESTAPI

DB_DATABASE = os.getenv('DB_DATABASE', 'bds')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'bds')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
REKENING_HOST = os.getenv('REKENING_HOST', 'localhost')
REKENING_PORT = int(os.getenv('REKENING_PORT', '8001'))
REKENING_URL = f'http://{REKENING_HOST}:{REKENING_PORT}'
API_HOST = os.getenv('NASABAH_HOST', 'localhost')
API_PORT = int(os.getenv('NASABAH_PORT', '8000'))


if __name__ == '__main__':
    logger = structlog.get_logger(service='nasabah')
    repo = NasabahRepository(DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD, logger)
    app = NasabahApp(repo, logger, rekening_URL=REKENING_URL)
    api = RESTAPI(API_HOST, API_PORT, app)
    api.run()
