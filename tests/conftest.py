import os
from code.mygram import MyTelegram

from pytest import fixture

app_tele = MyTelegram(os.getcwd() + '/code/sessions/valid')


@fixture
def tele():
    """Telegram sem session definida."""
    return MyTelegram


@fixture
def tele_ok():
    """Telegram com session ok."""
    return app_tele
