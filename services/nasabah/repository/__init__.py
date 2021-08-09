from typing import Union
from entities import NasabahIndividu
from asyncpg import Pool, create_pool
from structlog.types import FilteringBoundLogger

class NasabahRepository:
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

    async def create_nasabah(self, nasabah: NasabahIndividu) -> None:
        sql = 'INSERT INTO nasabah VALUES ($1, $2, $3, $4, $5);'
        try:
            async with self.pool.acquire() as conn:
                await conn.execute(sql, nasabah.cif, nasabah.ktp, nasabah.nama, nasabah.pekerjaan, nasabah.alamat)
        except Exception as e:
            self.log.error(f'Create nasabah failed: {str(e)}|{repr(e)}', nasabah=nasabah.dict())
            raise e
        self.log.info('Create nasabah success', nasabah=nasabah.dict())

    async def delete_nasabah(self, cif: str) -> None:
        sql = 'DELETE FROM nasabah WHERE cif = $1'
        try:
            async with self.pool.acquire() as conn:
                await conn.execute(sql, cif)
        except Exception as e:
            self.log.error(f'Delete nasabah failed: {str(e)}|{repr(e)}', cif=cif)
            raise e
        self.log.info('Delete nasabah success', cif=cif)