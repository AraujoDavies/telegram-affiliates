import logging
import os

from pyrogram import Client, enums
from pyrogram.types.messages_and_media.message import Message

# app = Client()


class MyTelegram:
    """
    NAME
        MyTelegram

    DESCTRIPTION
        Class that contains some methods to use Pyrogram API.
        ================================================
    """

    def __init__(self, session_path: str):
        """
        Instance class and store variables.

        Args:
            session_path (_str_): file that contains telegram session.

            chat_id: (_str_): chat id to interact.

        Example:
            >>> tele = MyTelegram(path) # instanciate class MyTelegram to interact with pyrogram API.
        """
        self.session_path = session_path
        # with Client(self.session_path) as app:
        #     me = app.get_me()
        self.app = Client(self.session_path)
        self.app.start()
        me = self.app.get_me()
        self.app.stop()
        logging.warning(f'Session Iniciada: {me}')

    def listar_chats(self):
        """Show chat_ids from some telegram account.

        Returns:
            chats: (_list_):
                list[0]: (_int_): is the chat_id number.

                list[1]: (_str_): is the name of the chats.

        Example:
            >>> tele = MyTelegram(session_path) # instanciate class MyTelegram to create new session # instanciate class MyTelegram to create new session

            >>> tele.listar_chats()
            ([1, 2, 3], ['chatname1', 'chatname2', 'chatname3'])
        """
        # with Client(self.session_path) as app:
        #     all_chats = app.get_dialogs()
        self.app.start()

        all_chats = self.app.get_dialogs()
        chat_ids = []
        chat_names = []
        list_chats = []
        for chat in all_chats:
            list_chats.append([chat.chat.id, chat.chat.title])
            chat_ids.append(chat.chat.id)
            chat_names.append(chat.chat.title)

        self.app.stop()

        logging.warning('Chat Name - Chat ID')
        for chat in list_chats:
            if chat[1] != None:
                logging.warning(f'{chat[1]} - {chat[0]}')

        logging.warning(
            '\nSelecione o ID do CHAT DESTINO e do CHAT ORIGEM e configure em config.env'
        )

        if bool(chat_ids):
            return chat_ids, chat_names
        else:
            return ([0], ['Não encontrou nenhum CHATS'])

    def enviar_msg(self, chat_id: int | str, msg: str) -> Message:
        """
        Send message and get message id.

        Args:
            chat_id: (_int_ | _str_): Target chat.

            msg (_str_): mensagem.

        Return:
            message_info: (_pyrogram.Message_): data info like message_id, date, username, etc.

        Example:
            >>> tele = MyTelegram(path) # instanciate class MyTelegram to interact with pyrogram API.

            >>> tele.enviar_msg(chat_id, msg)
            pyrogram.types.Message(id=18927, from_user=pyrogram.types.User(id=459457431, is_self=True, is_contact=True, is_mutual_contact=False, is_deleted=False,
            is_bot=False, is_verified=False, is_restricted=False, is_scam=False, is_fake=False, is_support=False, is_premium=False, first_name='Davies', status=pyrogram.enums.UserStatus.ONLINE, next_offline_date=datetime.datetime(2023, 11, 9, 13, 48, 10), username='Davies9', phone_number='5511930628076'), date=datetime.datetime(2023, 11, 9, 13, 44, 29), chat=pyrogram.types.Chat(id=459457431, type=pyrogram.enums.ChatType.PRIVATE, is_verified=False, is_restricted=False, is_scam=False, is_fake=False, is_support=False, username='MyUser', first_name='MyName'), mentioned=False, scheduled=False, from_scheduled=False, has_protected_content=False,
            text='hello!', outgoing=False)
        """
        # with Client(self.session_path) as app:
        #     msg_info = app.send_message(
        #         chat_id, (f'{msg}'), parse_mode=enums.ParseMode.HTML
        #     )
        self.app.start()
        msg_info = self.app.send_message(
            chat_id, (f'{msg}'), parse_mode=enums.ParseMode.HTML
        )
        self.app.stop()

        return msg_info

    def deletar_msg(self, chat_id: int | str, msg_id: int) -> int:
        """Delete message on telegram chat.

        Args:
            chat_id (int | str): chat alvo.
            msg_id (int): message id

        Returns:
            (_int_):
                0 -> delete fail.

                1 -> success delete.

        Example:
            >>> tele = MyTelegram(path) # instanciate class MyTelegram to interact with pyrogram API.
            >>> tele.deletar_msg(chat_id, msg_id)
            1 | 0
        """
        # with Client(self.session_path) as app:
        #     msg_info = app.delete_messages(chat_id=chat_id, message_ids=msg_id)
        self.app.start()
        msg_info = self.app.delete_messages(
            chat_id=chat_id, message_ids=msg_id
        )
        self.app.stop()

        return msg_info

    def resultado_msg(
        self, chat_id: int | str, reply_msg_id: int, msg: str
    ) -> Message:
        """
        Response a before message with markup.

        Args:
            chat_id (int | str):  chat alvo.
            reply_msg_id (int):  message to markup.
            msg (str): mensagem.

        Return:
            message_info: (_pyrogram.Message_): data info like message_id, date, username, etc.

        Example:
            >>> tele = MyTelegram(path) # instanciate class MyTelegram to interact with pyrogram API.
            >>> tele.resultado_msg(chat_id, msg)
            pyrogram.types.Message(id=123, from_user=pyrogram.types.User(id=123, is_self=True, is_contact=True, is_mutual_contact=False, is_deleted=False,
            is_bot=False, is_verified=False, is_restricted=False, is_scam=False, is_fake=False, is_support=False, is_premium=False, first_name='MyName', status=pyrogram.enums.UserStatus.ONLINE, next_offline_date=datetime.datetime(2023, 11, 9, 13, 48, 10), username='MyName', phone_number='5511987654321'), date=datetime.datetime(2023, 11, 9, 13, 44, 31), chat=pyrogram.types.Chat(id=123, type=pyrogram.enums.ChatType.PRIVATE, is_verified=False, is_restricted=False, is_scam=False, is_fake=False, is_support=False, username='MyName', first_name='MyName'), reply_to_message_id=123, reply_to_message=pyrogram.types.Message(id=123, from_user=pyrogram.types.User(id=123, is_self=True, is_contact=True, is_mutual_contact=False, is_deleted=False, is_bot=False, is_verified=False, is_restricted=False, is_scam=False, is_fake=False, is_support=False, is_premium=False, first_name='MyName', status=pyrogram.enums.UserStatus.ONLINE, next_offline_date=datetime.datetime(2023, 11, 9, 13, 48, 10), username='MyName', phone_number='5511987654321'), date=datetime.datetime(2023, 11, 9, 13, 44, 29), chat=pyrogram.types.Chat(id=459457431, type=pyrogram.enums.ChatType.PRIVATE, is_verified=False, is_restricted=False, is_scam=False, is_fake=False, is_support=False, username='MyTelegramName', first_name='MyName'), mentioned=False, scheduled=False, from_scheduled=False, has_protected_content=False, text='msg', outgoing=False), mentioned=False,
            scheduled=False, from_scheduled=False, has_protected_content=False, text='result-msg', outgoing=False)
        """
        # with Client(self.session_path) as app:
        #     msg_info = app.send_message(
        #         chat_id, f'{msg}', reply_to_message_id=reply_msg_id
        #     )
        self.app.start()
        msg_info = self.app.send_message(
            chat_id, f'{msg}', reply_to_message_id=reply_msg_id
        )
        self.app.stop()

        return msg_info


#     async def create_new_session(self, api_id, api_hash):
#         """
#         Create new session on telegram.

#         Args:
#             api_id: (_int_): to create telegram session.

#             api_hash (_str_): to create telegram session.

#         Example:
#             >>> tele = MyTelegram(session_path) # instanciate class MyTelegram to create new session # instanciate class MyTelegram to create new session
#  # instanciate class MyTelegram
#             >>> tele.create_new_session()
#         """
#         async with Client(self.session_path, api_id, api_hash) as app:
#             await app.send_message("me", "Robozinho de sinais configurado!")
