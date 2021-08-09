from pydantic import BaseModel

class Rekening(BaseModel):
    no_rekening: str = ''
    cif: str
    saldo: int