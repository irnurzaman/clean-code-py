import json
from typing import Tuple, Union
from uuid import uuid4
from structlog.types import FilteringBoundLogger

from repository import RekeningRepository
from entities import Rekening
from models import ReqCreateRekening


class RekeningApp:
    def __init__(self, repo: RekeningRepository, logger: FilteringBoundLogger) -> None:
        self.repo: RekeningRepository = repo
        self.logger: FilteringBoundLogger = logger

    def generate_no_rekening(self):
        return str(uuid4()).strip('-')

    async def create_rekening(self, request: ReqCreateRekening) -> Tuple[Union[None, Rekening], str]:
        rekening = Rekening(**request.dict())
        rekening.no_rekening = self.generate_no_rekening()

        try:
            await self.repo.create_rekening(rekening)
        except Exception:
            return None, 'No rekening sudah terdaftar'

        return rekening, ''