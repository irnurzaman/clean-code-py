import uvicorn
from typing import Dict, List
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from app import RekeningApp
from models import ReqCreateRekening
from entities import Rekening



class RESTAPI(FastAPI):
    def __init__(self, host: str, port: int, app: RekeningApp, debug: bool = False, title: str = "FastAPI", description: str = "", version: str = "0.1.0", openapi_url: str = "/openapi.json", servers: List[Dict[str, str]] = None) -> None:
        super().__init__(debug=debug, title=title, description=description, version=version, openapi_url=openapi_url, servers=servers)
        self.app: RekeningApp = app
        self.host: str = host
        self.port: int = port

        @self.on_event('startup')
        async def startup():
            await self.app.repo.init_db()

        @self.post('/rekening', status_code=status.HTTP_200_OK, response_model=Rekening)
        async def create_rekening(request: ReqCreateRekening):
            rekening, remark = await self.app.create_rekening(request)
            if rekening is None:
                return JSONResponse({'remark': remark}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
            return rekening

    def run(self):
        uvicorn.run(self, host= self.host, port= self.port, loop='asyncio')