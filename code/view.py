import json
import logging
import os

import dotenv
from main import app
from mygram import MyTelegram
from pyrogram.errors.exceptions.bad_request_400 import UsernameInvalid

dotenv.load_dotenv()


@app.get('/health')
def healthcheck():
    return {'healthcheck': 'OK'}


# test_envio
@app.get('/teste-envio/{telegram_username}')
async def teste_de_envio(telegram_username: str):
    try:
        session = os.getenv('ABSOLUTE_SESSION_PATH')
        tele = MyTelegram(session_path=session)
        # tele.listar_chats()
        tele_msg = await tele.enviar_msg(
            telegram_username,
            'Oi, teste efetuado com sucesso atráves da API-AFFILIATES',
        )
        content = str(tele_msg)
        json_acceptable_string = content.replace("'", '"')
        content = json.loads(json_acceptable_string)

        return content
    except AttributeError as error:   # SESSION INVALIDA
        return {'SESSION_ERROR': str(error)}
    except UsernameInvalid as error:   # CHAT INVALIDO
        return {'CHAT_ERROR': str(error)}
    # except ValueError as error: #
    #     return {"SERVER_ERROR": "Servidor falhou ao processar solicitação"}
    except Exception as error:
        logging.error(error.with_traceback())
        return {'UNKNOW_ERROR': str(error)}


# listar_chats
@app.post('/listar-chats')
async def listar_todos_chats_do_usuario():
    try:
        session = os.getenv('ABSOLUTE_SESSION_PATH')
        tele = MyTelegram(session_path=session)
        chats = await tele.listar_chats()
        return chats
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}


# enviar_mensagem
@app.post('/enviar')
async def enviar_mensagem():
    try:
        session = os.getenv('ABSOLUTE_SESSION_PATH')
        tele = MyTelegram(session_path=session)
        chats = await tele.enviar_msg('me', 'enviar-msg route')
        return chats
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}


# deletar_mensagem
@app.post('/deletar')
async def deletar_mensagem():
    try:
        session = os.getenv('ABSOLUTE_SESSION_PATH')
        tele = MyTelegram(session_path=session)
        chats = await tele.deletar_msg('me', 1)
        return chats
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}


# enviar_mensagem_com_marcacao
@app.post('/responder')
async def enviar_respondendo_msg_anterior():
    try:
        session = os.getenv('ABSOLUTE_SESSION_PATH')
        tele = MyTelegram(session_path=session)
        chats = await tele.resultado_msg('me', 1, 'enviar-msg-mark')
        return chats
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}
