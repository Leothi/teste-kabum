from pydantic import BaseModel, Field
from typing import List

from api.models import SuccessResponse


class DimensaoBase(BaseModel):
    altura: int = Field(..., description="Altura de entrada.")
    largura: int = Field(..., description="Largura de entrada.")


class FreteInput(BaseModel):
    dimensao: DimensaoBase
    peso: int = Field(..., description="Peso de entrada.")


class FreteBase(BaseModel):
    nome: str
    valor_frete: float
    prazo_dias: int


class FreteResponse(SuccessResponse):
    """Response model to /set_notifications on /cfg prefix"""
    List[FreteBase]
