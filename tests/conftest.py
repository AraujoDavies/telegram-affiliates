from code.mygram import MyTelegram

from pytest import fixture


@fixture
def tele():
    return MyTelegram
