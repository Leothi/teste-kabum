from fastapi import APIRouter
from loguru import logger

from api.models.frete import FreteInput, FreteResponse
from api.modules.frete import CalculadorFrete

router = APIRouter()


@router.post('/calcular', response_model=FreteResponse, summary="Cálculo do frete.")
def router_get_notification(body: FreteInput) -> dict:
    """Cálcula o frete de acordo com as características do produto."""

    logger.log('LOG ROTA', "Chamada rota /calcular.")
    return {'lista_fretes': CalculadorFrete().criar_lista_fretes(body.dict())}
