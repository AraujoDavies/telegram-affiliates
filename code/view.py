import json
import logging
import os

import dotenv
from danticmodels import SessionItem
from main import app
from mygram import MyTelegram
from pyrogram.errors.exceptions.bad_request_400 import UsernameInvalid

dotenv.load_dotenv(override=True)

sessions = os.getenv('ABSOLUTE_SESSION_PATH')

from views_helpers import session_is_ok


@app.get('/healthcheck')
def healthcheck():
    return {'healthcheck': 'OK'}


# @app.get('/path') # DEBUG
# def path():
#     # dotenv.load_dotenv(override=True)
#     return os.getenv('ABSOLUTE_SESSION_PATH')

# test_envio
@app.get('/teste-envio/{telegram_username}/{session_file}')
async def teste_de_envio(telegram_username: str, session_file: str):
    """Invokes send message in telegram api.

    Args:
        telegram_username: who will receive the message, (me = my own telegram).

        session_file: some session in sessions path.

    Returns:
        dict: dict with id, text and date.
    """
    try:
        session_ok = session_is_ok(session_file=session_file)
        if session_ok:   # se o arquivo existe no diretorio
            session = sessions + session_file   # concatena dir + file.session
            tele = MyTelegram(session_path=session)

            chats = await tele.enviar_msg(
                telegram_username,
                'Oi, teste efetuado com sucesso atráves da API-AFFILIATES',
            )

            # chats = str(tele_msg)
            # json_acceptable_string = content.replace("'", '"')
            # content = json.loads(json_acceptable_string)

            content_dict = {}
            content_dict['id'] = chats.id
            content_dict['date'] = chats.date
            content_dict['text'] = chats.text
            return content_dict

        return {'SESSION_ERROR': 'SESSION FILE DOESNT EXISTS'}
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
async def listar_todos_chats_do_usuario(session_item: SessionItem):
    """Invokes list chats in telegram api.

    Args:
        session_item (SessionItem):

            request_body = {
                session_item.session_file,
            }

    Returns:
        dict: dict contained all chats, example: {chat_name1: chat_id1, chat_name2: chat_id2}
    """
    try:
        session_ok = session_is_ok(session_file=session_item.session_file)

        if session_ok:   # se o arquivo existe no diretorio
            session = (
                sessions + session_item.session_file
            )   # concatena dir + file.session
            tele = MyTelegram(session_path=session)
            chats = await tele.listar_chats()
            return chats
        return {'SESSION_ERROR': 'SESSION FILE DOESNT EXISTS'}
    except AttributeError as error:   # SESSION INVALIDA
        return {'SESSION_ERROR': str(error)}
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}


# enviar_mensagem
@app.post('/enviar')
async def enviar_mensagem(session_item: SessionItem):
    """Invokes send message in telegram api.

    Args:
        session_item (SessionItem):

            request_body = {
                session_item.session_file,
                session_item.chat_id,
                session_item.message_text,
            }

    Returns:
        dict: dict with id, text and date.
    """
    try:
        session_ok = session_is_ok(session_file=session_item.session_file)

        if session_ok:   # se o arquivo existe no diretorio
            session = (
                sessions + session_item.session_file
            )   # concatena dir + file.session
            tele = MyTelegram(session_path=session)
            chats = await tele.enviar_msg(
                session_item.chat_id, session_item.message_text
            )
            content_dict = {}
            content_dict['id'] = chats.id
            content_dict['date'] = chats.date
            content_dict['text'] = chats.text
            return content_dict

        return {'SESSION_ERROR': 'SESSION FILE DOESNT EXISTS'}
    except AttributeError as error:   # SESSION INVALIDA
        return {'SESSION_ERROR': str(error)}
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}


# enviar_mensagem_com_marcacao
@app.post('/responder')
async def enviar_respondendo_msg_anterior(session_item: SessionItem):
    """Invokes reply message in telegram api.

    Args:
        session_item (SessionItem):

            request_body = {
                session_item.session_file,
                session_item.chat_id,
                session_item.message_id (if dont found, will send without reply),
                session_item.message_text,
            }

    Returns:
        dict: dict with id, text and date.
    """
    try:
        session_ok = session_is_ok(session_file=session_item.session_file)
        if session_ok:   # se o arquivo existe no diretorio
            session = (
                sessions + session_item.session_file
            )   # concatena dir + file.session
            tele = MyTelegram(session_path=session)
            chats = await tele.resultado_msg(
                session_item.chat_id,
                session_item.message_id,
                session_item.message_text,
            )

            content_dict = {}
            content_dict['id'] = chats.id
            content_dict['date'] = chats.date
            content_dict['text'] = chats.text
            return content_dict
        return {'SESSION_ERROR': 'SESSION FILE DOESNT EXISTS'}
    except AttributeError as error:   # SESSION INVALIDA
        return {'SESSION_ERROR': str(error)}
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}


# deletar_mensagem
@app.post('/deletar')
async def deletar_mensagem(session_item: SessionItem):
    """Invokes delete message in telegram api.

    Args:
        session_item (SessionItem):

            request_body = {
                session_item.session_file,
                session_item.chat_id,
                session_item.message_id,
            }

    Returns:
        dict: SUCCESS = 1 if delete happen or 0 if not happen.
    """
    try:
        session_ok = session_is_ok(session_file=session_item.session_file)

        if session_ok:   # se o arquivo existe no diretorio
            session = (
                sessions + session_item.session_file
            )   # concatena dir + file.session
            tele = MyTelegram(session_path=session)
            chats = await tele.deletar_msg(
                session_item.chat_id, session_item.message_id
            )

            return {'SUCCESS': int(chats)}
        return {'SESSION_ERROR': 'SESSION FILE DOESNT EXISTS'}
    except AttributeError as error:   # SESSION INVALIDA
        return {'SESSION_ERROR': str(error)}
    except Exception as error:
        return {'UNKNOW_ERROR': str(error)}
