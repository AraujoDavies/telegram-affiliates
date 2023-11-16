import os
from code.main import app as app_fast
from code.mygram import MyTelegram

import dotenv
from httpx import AsyncClient
from pytest import fixture

dotenv.load_dotenv()

# mygram fixtures
@fixture
def tele():
    """Telegram com session ok."""
    tele = MyTelegram(os.getenv('ABSOLUTE_SESSION_PATH'))
    return tele


# fastapi fixtures
@fixture(
    scope='session'
)   # essa func serve para evitar erro de threading na request via teste
def anyio_backend():
    return 'asyncio'


@fixture(scope='session')
async def client():
    async with AsyncClient(
        app=app_fast, base_url='http://127.0.0.1:8000/'
    ) as client:
        print('Client is ready')
        yield client
