from logging import log
import os
import asyncpg
import structlog
import asyncpg

from repository import NasabahRepository
from app import NasabahApp
from api import RESTAPI

DB_DATABASE = os.getenv('DB_DATABASE', 'bds')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
REKENING_URL = os.getenv('REKENING_URL', 'http://localhost:8001')
API_HOST = os.getenv('API_HOST', 'localhost')
API_PORT = int(os.getenv('API_PORT', '8000'))

if __name__ == '__main__':
    logger = structlog.make_filtering_bound_logger(20)
    db_pool = asyncpg.create_pool(database=DB_DATABASE, user=DB_USER, host=DB_HOST, password=DB_PASSWORD)
    repo = NasabahRepository(db_pool, logger)
    app = NasabahApp(repo, logger, rekening_URL=REKENING_URL)
    api = RESTAPI(API_HOST, API_PORT, app)
    api.run()