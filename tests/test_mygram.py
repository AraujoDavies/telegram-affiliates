import pytest


def test_session_que_nao_funciona(tele):
    with pytest.raises(AttributeError) as exc_info:
        tele(session_path='invalid')
    assert 'The API key is required for new authorizations.' in str(
        exc_info.value
    )


def test_session_que_esta_ok(tele_ok):
    assert 'mygram.MyTelegram' in str(type(tele_ok))


def test_listar_id_dos_chats(tele_ok):
    chats = tele_ok.listar_chats()
    assert (
        len(chats) == 2
        and len(chats[0]) > 1
        and len(chats[0]) == len(chats[1])
    )


def test_enviar_mensagem(tele_ok):
    global id_msg   # global pois sera usada nos testes a seguir
    id_msg = tele_ok.enviar_msg('me', 'pytest - robozinho afiliates')
    assert type(id_msg.id) == int


def test_enviar_resultado(tele_ok):
    global result
    result = tele_ok.resultado_msg(
        'me', id_msg.id, 'result - pytest - robozinho afiliates'
    )
    assert type(result.id) == int


def test_apagar_mensagem(tele_ok):
    assert (
        tele_ok.deletar_msg('me', id_msg.id) == 1
    )   # delete retorna se deletar mesmo = 1 | se nao existir a mensagem = 0
    assert (
        tele_ok.deletar_msg('me', result.id) == 1
    )   # delete retorna se deletar mesmo = 1 | se nao existir a mensagem = 0
