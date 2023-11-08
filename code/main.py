import asyncio

from mygram import MyTelegram

if __name__ == '__2main__':
    db_session = 'sessions/' + 'tigeroficialnew'
    db_chat_id = -1001262067125

    session_from_db = 'sessions/' + 'tigeroficialnew'
    tele = MyTelegram(session_path=session_from_db)
    session_from_db = 'sessions/' + 'tigeroficialnew2'
    tele2 = MyTelegram(session_path=session_from_db)
    session_from_db = 'sessions/' + 'tigeroficialnew3'
    tele3 = MyTelegram(session_path=session_from_db)
    # asyncio.run(tele.create_new_session())
    # chats = tele.get_chats()

    # if db_chat_id in chats:
    #     # OK - Pode ir
    # else:
    #     # CHAT que está tentando enviar nao existe no telegram
