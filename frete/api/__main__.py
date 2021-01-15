import uvicorn

from api.settings import envs


def start():
    uvicorn.run('frete:app',
                host=envs.FASTAPI_HOST, port=envs.FASTAPI_PORT,
                debug=envs.FASTAPI_DEBUG, reload=envs.FASTAPI_RELOAD, access_log=envs.FASTAPI_ACCESS_LOG)


if __name__ == '__main__':
    start()
