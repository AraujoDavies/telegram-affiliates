import logging
import os

from pyrogram import Client, enums


class MyTelegram:
    """
    NAME
        MyTelegram

    DESCTRIPTION
        Class that contains some methods to use Pyrogram API.
        ================================================
    """

    def __init__(self, session_path: str, chat_id: str = 'me'):
        """
        Instance class and store variables.

        Args:
            session_path (_str_): file that contains telegram session.

            chat_id: (_str_): chat id to interact.

        Example:
            >>> tele = MyTelegram(path) # instanciate class MyTelegram to send messages.

            >>> tele = MyTelegram(session_path, chat_id) # instanciate class MyTelegram to create new session # instanciate class MyTelegram to create new session.
        """
        print(os.getcwd())

        try:   # test session
            self.session_path = session_path
            with Client(self.session_path) as app:
                app.get_dialogs()
            self.app = Client(self.session_path)
        except Exception as error:
            logging.critical(error)
            return False

    #     async def create_new_session(self, api_id, api_hash):
    #         """
    #         Create new session on telegram.

    #         Args:
    #             api_id: (_int_): to create telegram session.

    #             api_hash (_str_): to create telegram session.

    #         Example:
    #             >>> tele = MyTelegram(session_path, chat_id) # instanciate class MyTelegram to create new session # instanciate class MyTelegram to create new session
    #  # instanciate class MyTelegram
    #             >>> tele.create_new_session()
    #         """
    #         async with Client(self.session_path, api_id, api_hash) as app:
    #             await app.send_message("me", "Robozinho de sinais configurado!")

    def get_chats(self):
        """Show chat_ids from some telegram account

               Returns:
                   chats: (_list_):
                       list[0]: (_int_): is the chat_id number.

                       list[1]: (_str_): is the name of the chats.

               Example:
                   >>> tele = MyTelegram(session_path, chat_id) # instanciate class MyTelegram to create new session # instanciate class MyTelegram to create new session
        # instanciate class MyTelegram
                   >>> tele.create_new_session()
        """
        with Client(self.session_path) as app:
            all_chats = app.get_dialogs()

            chat_ids = []
            chat_names = []
            list_chats = []
            for chat in all_chats:
                list_chats.append([chat.chat.id, chat.chat.title])
                chat_ids.append(chat.chat.id)
                chat_names.append(chat.chat.title)

        logging.warning('Chat Name - Chat ID')
        for chat in list_chats:
            if chat[1] != None:
                logging.warning(f'{chat[1]} - {chat[0]}')

        logging.warning(
            '\nSelecione o ID do CHAT DESTINO e do CHAT ORIGEM e configure em config.env'
        )

        return chat_ids, chat_names

    def enviar_no_telegram(self, chat_id, msg):
        """
        Send message and get message id.

        Params
        """
        with Client(self.session_path) as app:
            app.start()
            app.send_message(
                chat_id, (f'{msg}'), parse_mode=enums.ParseMode.HTML
            )
            for message in app.get_chat_history(chat_id):
                id = message.id
                break
            app.stop()
        return id

    def deletar_msg(self, chat_id, msg_id):
        with Client(self.session_path) as app:
            app.start()
            app.delete_messages(chat_id=chat_id, message_ids=msg_id)
            for message in app.get_chat_history(chat_id):
                id = message.id
                break
            app.stop()
        return id

    async def resultado_da_entrada(self, chat_id, reply_msg_id, msg):
        """
        responde a msg de entrada com o resultado(green/red)
        """
        with Client(self.session_path) as app:
            await app.start()
            await app.send_message(
                chat_id, f'{msg}', reply_to_message_id=reply_msg_id
            )
            await app.stop()
        # app.run(resultado_da_entrada(chat_id, reply_msg_id, msg))
