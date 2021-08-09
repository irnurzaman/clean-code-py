import json
from typing import Tuple, Union
from uuid import uuid4
from structlog.types import FilteringBoundLogger
from aiohttp import ClientSession

from repository import NasabahRepository
from entities import NasabahIndividu, NasabahBadanUsaha
from models import ReqCreateNasabahIndividu


class NasabahApp:
    def __init__(self, repo: NasabahRepository, logger: FilteringBoundLogger, rekening_URL: str) -> None:
        self.repo: NasabahRepository = repo
        self.logger: FilteringBoundLogger = logger
        self.rekening_URL: str = rekening_URL
        self.client: Union[ClientSession, None] = None
        
        

    def generate_cif(self):
        return str(uuid4()).strip('-')

    async def create_nasabah(self, request: ReqCreateNasabahIndividu) -> Tuple[Union[None, NasabahIndividu], str]:
        nasabah = NasabahIndividu(**request.dict())
        nasabah.cif = self.generate_cif()

        try:
            await self.repo.create_nasabah(nasabah)
        except Exception:
            return None, 'NIK sudah terdaftar'

        rekening_request = {'cif': nasabah.cif, 'saldo': request.setoran}
        async with self.client.post(f'{self.rekening_URL}/rekening', json=rekening_request) as resp:
            response = await resp.json()
            if resp.status != 200:
                remark = response['remark'] 
                try:
                    await self.repo.delete_nasabah(nasabah.cif)
                except Exception:
                    pass
                return None, remark
            else:
                return nasabah, ''