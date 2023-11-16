from pydantic import BaseModel

# from typing import Union


class SessionItem(BaseModel):
    session_file: str
    chat_id: str = 'me'
    message_id: int = 1
    message_text: str = '.'
