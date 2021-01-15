from pydantic import BaseModel, Field
from typing import List

from api.models import SuccessResponse


class DimensaoBase(BaseModel):
    altura: int = Field(..., description="Altura de entrada (cm).", example=102)
    largura: int = Field(..., description="Largura de entrada (g).", example=40)


class FreteInput(BaseModel):
    dimensao: DimensaoBase
    peso: int = Field(..., description="Peso de entrada.", example=400)


class FreteBase(BaseModel):
    nome: str = Field(..., description="Nome do frete.", example="Entrega Ninja")
    valor_frete: float = Field(..., description="Valor final do frete.", example=12.00)
    prazo_dias: int = Field(..., description="Prazo final do frete.", example=6)


class FreteResponse(SuccessResponse):
    """Response model to /set_notifications on /cfg prefix"""
    lista_fretes: List[FreteBase]
