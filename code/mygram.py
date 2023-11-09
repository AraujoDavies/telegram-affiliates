import logging
import os

from pyrogram import Client, enums

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
            >>> tele = MyTelegram(path) # instanciate class MyTelegram to send messages.

            >>> tele = MyTelegram(session_path) # instanciate class MyTelegram to create new session # instanciate class MyTelegram to create new session.
        """
        self.session_path = session_path
        # with Client(self.session_path) as app:
        #     me = app.get_me()
        self.app = Client(self.session_path)
        self.app.start()
        me = self.app.get_me()
        self.app.stop()
        logging.warning(f'Session Iniciada: {me}')

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

    def listar_chats(self):
        """Show chat_ids from some telegram account

               Returns:
                   chats: (_list_):
                       list[0]: (_int_): is the chat_id number.

                       list[1]: (_str_): is the name of the chats.

               Example:
                   >>> tele = MyTelegram(session_path) # instanciate class MyTelegram to create new session # instanciate class MyTelegram to create new session
        # instanciate class MyTelegram
                   >>> tele.create_new_session()
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

    def enviar_msg(self, chat_id: int | str, msg: str):
        """
        Send message and get message id.

        Params
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

    def deletar_msg(self, chat_id: int | str, msg_id: int):
        # with Client(self.session_path) as app:
        #     msg_info = app.delete_messages(chat_id=chat_id, message_ids=msg_id)
        self.app.start()
        msg_info = self.app.delete_messages(
            chat_id=chat_id, message_ids=msg_id
        )
        self.app.stop()

        return msg_info

    def resultado_msg(self, chat_id: int | str, reply_msg_id: int, msg: str):
        """
        responde a msg de entrada com o resultado(green/red)
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
