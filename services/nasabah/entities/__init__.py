from pydantic import BaseModel
from datetime import datetime

class NasabahIndividu(BaseModel):
    cif: str
    ktp: str
    nama: str
    pekerjaan: str
    alamat: str

class NasabahBadanUsaha(BaseModel):
    cif: str
    nama: str
    pemilik: str
    bidang: str
