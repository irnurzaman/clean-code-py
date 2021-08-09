from datetime import datetime
from pydantic import BaseModel

class ReqCreateNasabahIndividu(BaseModel):
    ktp: str
    nama: str
    pekerjaan: str
    alamat: str
    setoran: int