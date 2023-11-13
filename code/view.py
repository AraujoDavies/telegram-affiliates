import json
import logging
import os

import dotenv
from main import app
from mygram import MyTelegram
from pyrogram.errors.exceptions.bad_request_400 import UsernameInvalid

dotenv.load_dotenv()


@app.get('/health')
def hello():
    return {'Healthcheck': 'OK'}


# test_envio
@app.get('/teste-envio/{telegram_username}')
async def teste_envio(telegram_username: str):
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
async def listar_chats():
    try:
        session = os.getenv('ABSOLUTE_SESSION_PATH')
        tele = MyTelegram(session_path=session)
        chats = await tele.listar_chats()
        return chats
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}


# enviar_mensagem
# deletar_mensagem
# enviar_mensagem_com_marcando
