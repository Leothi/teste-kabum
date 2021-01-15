import sys

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from api.settings import envs
from api.routes import frete
from api.models import DEFAULT_RESPONSES_JSON
from api.modules.default.middleware import Middleware
from api.exceptions import ExceptionHandler

__version__ = '1.0.0'

# Configuração do Logger
logger.configure(
    handlers=[
        {
            "sink": sys.stdout,
            "level": 10,
            "format": envs.LOGURU_FORMAT
        }
    ]
)

# Criação de Levels
logger.level('REQUEST RECEBIDA', no=37, color="<yellow>")
logger.level('REQUEST FINALIZADA', no=38, color="<yellow>")
logger.level('LOG ROTA', no=39, color="<light-green>")

# Saída para arquivo logger
logger.add("./logs/teste.log", level=0,
           format=envs.LOGURU_FORMAT, rotation='500 MB')
logger.add("./logs/teste_error.log", level=40,
           format=envs.LOGURU_FORMAT, rotation='500.MB')

# Instância API
app = FastAPI(title='Teste Python Kabum', description="Teste técnico para processo seletivo da Kabum.",
              version=__version__)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(frete.router,
                   prefix='/frete',
                   tags=["Cálculo de frete"],
                   responses={**DEFAULT_RESPONSES_JSON}
                   )


# Módulos da API
Middleware(app)
ExceptionHandler(app)
