from fastapi import APIRouter
from loguru import logger

from api.models.frete import FreteInput


router = APIRouter()


@router.post('/calcular', summary="Listagem das configurações.")
def router_get_notification(body: FreteInput) -> dict:
    """Lista todas as configurações do BOT Telegram."""

    logger.log('LOG ROTA', "Chamada rota /get_all.")
    return {**body.dict()}
