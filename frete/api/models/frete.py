from pydantic import BaseModel, Field
from typing import List

from api.models import SuccessResponse


class DimensaoBase(BaseModel):
    """ Modelo base para dimensão """
    altura: int = Field(..., description="Altura de entrada (cm).", example=102)
    largura: int = Field(..., description="Largura de entrada (cm).", example=40)


class FreteInput(BaseModel):
    """ Modelo para Input de frete """
    dimensao: DimensaoBase
    peso: int = Field(..., description="Peso de entrada (g).", example=400)


class FreteBase(BaseModel):
    """ Modelo base para resposta de frete"""
    nome: str = Field(..., description="Nome do frete.", example="Entrega Ninja")
    valor_frete: float = Field(..., description="Valor final do frete.", example=12.00)
    prazo_dias: int = Field(..., description="Prazo final do frete.", example=6)


class FreteResponse(SuccessResponse):
    """Modelo de resposta para /calcular"""
    lista_fretes: List[FreteBase]
