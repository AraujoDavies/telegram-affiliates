import asyncio
import logging
import os

from fastapi import FastAPI
from mygram import MyTelegram

app = FastAPI()

from view import *

# if __name__ == '__main2__':
# session_from_db = 'valid'
# # criar uma lista com as sessions existentes:
# sessions_validas = os.listdir(os.getcwd() + '/code/sessions')
# logging.warning('Sessões disponíves: \n%s', sessions_validas)
# # verifica se a session do cara existe
# #     if session_from_db + '.session' in sessions_validas:
# session_from_db = 'sessions/' + session_from_db
#         tele = MyTelegram(session_path=session_from_db)
#         tele.listar_chats()

#         # tele_msg = tele.enviar_msg('me', 'pytest')

#         tele_msg = tele.app.run(tele.enviar_msg('me', 'hahahaah'))

#         # tele_result = tele.resultado_msg('me', tele_msg.id, 'result-pytest')
#         # tele_delete = tele.deletar_msg(
#         #     'me', tele_msg.id
#         # )   # retorno sempre == 1
#     else:
#         logging.error('SESSÂO NÃO EXISTE.')
