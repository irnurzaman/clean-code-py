import uvicorn
from typing import Dict, List
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from aiohttp import ClientSession

from app import NasabahApp
from models import ReqCreateNasabahIndividu
from entities import NasabahIndividu



class RESTAPI(FastAPI):
    def __init__(self, host: str, port: int, app: NasabahApp, debug: bool = False, title: str = "FastAPI", description: str = "", version: str = "0.1.0", openapi_url: str = "/openapi.json", servers: List[Dict[str, str]] = None) -> None:
        super().__init__(debug=debug, title=title, description=description, version=version, openapi_url=openapi_url, servers=servers)
        self.app: NasabahApp = app
        self.host: str = host
        self.port: int = port

        @self.on_event('startup')
        async def startup():
            self.app.client = ClientSession()
            await self.app.repo.init_db()

        @self.post('/nasabah', status_code=status.HTTP_200_OK, response_model=NasabahIndividu)
        async def create_nasabah(request: ReqCreateNasabahIndividu):
            nasabah, remark = await self.app.create_nasabah(request)
            if nasabah is None:
                return JSONResponse({'remark': remark}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
            return nasabah

    def run(self):
        uvicorn.run(self, host= self.host, port= self.port, loop='asyncio')