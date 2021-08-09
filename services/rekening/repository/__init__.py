from typing import Union
from entities import Rekening
from asyncpg import Pool, create_pool
from structlog.types import FilteringBoundLogger

class RekeningRepository:
    def __init__(self, host: str, db: str, user: str, password: str, logger: FilteringBoundLogger) -> None:
        self.host: str = host
        self.db: str = db
        self.user: str = user
        self.password: str = password
        self.pool: Union[Pool, None] = None
        self.log: FilteringBoundLogger = logger

    async def init_db(self):
        self.pool  = await create_pool(database=self.db, user=self.user, host=self.host, password=self.password)
        self.log.info('connected to DB')

    async def create_rekening(self, rekening: Rekening) -> None:
        insert_sql = 'INSERT INTO rekening VALUES ($1, $2);'
        relation_sql = 'INSERT INTO rekening_nasabah VALUES ($1, $2)'
        try:
            async with self.pool.acquire() as conn:
                await conn.execute(insert_sql, rekening.no_rekening, rekening.saldo)
                await conn.execute(relation_sql, rekening.cif, rekening.no_rekening)
        except Exception as e:
            self.log.error(f'Create rekening failed: {str(e)}|{repr(e)}', rekening=rekening.dict())
            raise e
        self.log.info('Create rekening success', rekening=rekening.dict())

    async def delete_rekening(self, no_rekening: str) -> None:
        sql = 'DELETE FROM rekening WHERE no_rekening = $1'
        try:
            async with self.pool.acquire() as conn:
                await conn.execute(sql, no_rekening)
        except Exception as e:
            self.log.error(f'Delete rekening failed: {str(e)}|{repr(e)}', no_rekening=no_rekening)
            raise e
        self.log.info('Delete rekening success', no_rekening=no_rekening)