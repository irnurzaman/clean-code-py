from pydantic import BaseModel

class ReqCreateRekening(BaseModel):
    cif: str
    saldo: int