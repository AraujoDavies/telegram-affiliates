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
        # logging.warning('session_path')
        # self.app.start()
        # try:
        #     me = self.app.get_me()
        # finally:
        #     self.app.stop()
        # logging.warning(f'Session Iniciada: {me}')

    async def listar_chats(self):
        """Show chat_ids from some telegram account.

        Returns:
            chats: (_dict_):
                {chat_name(_str_): chat_id(_int_)}

        Example:
            >>> tele = MyTelegram(session_path) # instanciate class MyTelegram to create new session # instanciate class MyTelegram to create new session

            >>> tele.listar_chats()
            {'chatname1': chatid1, 'chatname2': chatid2, 'chatname3': chatid3}
        """
        await self.app.start()
        try:
            # all_chats = self.app.get_dialogs()
            list_chats = {}
            # Iterate through all dialogs
            async for dialog in self.app.get_dialogs():
                list_chats[dialog.chat.title] = dialog.chat.id
        finally:
            await self.app.stop()

        # logging.warning('Chat Name - Chat ID')

        # for key in list_chats:
        #     logging.warning('%s: %s', key, list_chats[key])

        # logging.warning(
        #     '\nSelecione o ID do CHAT DESTINO e do CHAT ORIGEM e configure em config.env'
        # )

        return list_chats

    async def enviar_msg(self, chat_id: int | str, msg: str) -> Message:
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
        # async with Client(self.session_path) as app:
        #     msg_info = await app.send_message(
        #         chat_id, (f'{msg}'), parse_mode=enums.ParseMode.HTML
        #     )
        await self.app.start()
        try:
            msg_info = await self.app.send_message(
                chat_id, (f'{msg}'), parse_mode=enums.ParseMode.HTML
            )
        finally:
            await self.app.stop()

        return msg_info

    async def deletar_msg(self, chat_id: int | str, msg_id: int) -> int:
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
        await self.app.start()
        try:
            msg_info = await self.app.delete_messages(
                chat_id=chat_id, message_ids=msg_id
            )
        finally:
            await self.app.stop()

        return msg_info

    async def resultado_msg(
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
        await self.app.start()
        try:
            msg_info = await self.app.send_message(
                chat_id, f'{msg}', reply_to_message_id=reply_msg_id
            )
        finally:
            await self.app.stop()

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
