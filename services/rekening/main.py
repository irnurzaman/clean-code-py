from logging import log
import os
import asyncpg
import structlog
import asyncpg

from repository import RekeningRepository
from app import RekeningApp
from api import RESTAPI

DB_DATABASE = os.getenv('DB_DATABASE', 'bds')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'bds')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
API_HOST = os.getenv('REKENING_HOST', 'localhost')
API_PORT = int(os.getenv('REKENING_PORT', '8001'))

if __name__ == '__main__':
    logger = structlog.get_logger(service='rekening')
    repo = RekeningRepository(DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD, logger)
    app = RekeningApp(repo, logger)
    api = RESTAPI(API_HOST, API_PORT, app)
    api.run()