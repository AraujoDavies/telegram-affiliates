import asyncio
import os
from code.main import MyTelegram

import dotenv
import pytest

dotenv.load_dotenv()

####### INIT FIXTURES #######


@pytest.fixture  # dedicated fixture decorator that will do the right thing
async def listar_id_dos_chats():
    tele = MyTelegram(os.getenv('ABSOLUTE_SESSION_PATH'))
    chats = await tele.listar_chats()
    return chats


@pytest.fixture  # dedicated fixture decorator that will do the right thing
async def enviar_msg():
    tele = MyTelegram(os.getenv('ABSOLUTE_SESSION_PATH'))
    msg_info = await tele.enviar_msg('me', 'pytest - robozinho afiliates')
    return msg_info


@pytest.fixture  # dedicated fixture decorator that will do the right thing
async def enviar_resultado():
    tele = MyTelegram(os.getenv('ABSOLUTE_SESSION_PATH'))
    msg_info = await tele.resultado_msg(
        'me', id_msg.id, 'result - pytest - robozinho afiliates'
    )
    return msg_info


@pytest.fixture
async def apagar_mensagem():
    tele = MyTelegram(os.getenv('ABSOLUTE_SESSION_PATH'))
    # delete retorna se deletar mesmo = 1 | se nao existir a mensagem = 0
    apaga_msg = await tele.deletar_msg('me', id_msg.id)
    apaga_resultado = await tele.deletar_msg('me', result.id)
    return (apaga_msg, apaga_resultado)


####### END FIXTURES #######


def test_session_que_esta_ok(tele):
    assert 'mygram.MyTelegram' in str(type(tele))


@pytest.mark.asyncio
async def test_listar_id_dos_chats(listar_id_dos_chats):
    rets = await asyncio.gather(listar_id_dos_chats)
    rets = rets[0].keys()
    assert 'Me andme' in rets


@pytest.mark.asyncio
async def test_enviar_mensagem(enviar_msg):
    global id_msg   # global pois sera usada nos testes a seguir
    id_msg = await asyncio.gather(enviar_msg)
    id_msg = id_msg[0]
    assert type(id_msg.id) == int


@pytest.mark.asyncio
async def test_enviar_resultado(enviar_resultado):
    global result
    result = await asyncio.gather(enviar_resultado)
    result = result[0]
    assert type(result.id) == int


@pytest.mark.asyncio
async def test_deletar_msg(apagar_mensagem):
    result = await asyncio.gather(apagar_mensagem)
    result = result[0]
    assert result == (1, 1)
