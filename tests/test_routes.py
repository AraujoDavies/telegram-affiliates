from urllib import response

import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_healthecheck(client: AsyncClient):
    response = await client.get('/healthcheck')
    assert response.json() == {'healthcheck': 'OK'}


@pytest.mark.anyio
async def test_route_teste_envio(client: AsyncClient):
    response = await client.get('/teste-envio/valid')
    assert response.status_code == 200
    assert (
        'Oi, teste efetuado com sucesso atráves da API-AFFILIATES'
        == response.json()['text']
    )


# @pytest.mark.anyio
# async def test_route_envio_chat_error(client: AsyncClient):
#     response = await client.get('/teste-envio/valid')
#     assert response.status_code == 200
#     assert (
#         'Telegram says: [400 USERNAME_INVALID] - The username is invalid'
#         in response.json()['CHAT_ERROR']
#     )


@pytest.mark.anyio
async def test_route_envio_com_invalid_session(client: AsyncClient):
    response = await client.get('/teste-envio/invalid')
    assert response.status_code == 200
    assert (
        'The API key is required for new authorizations. More info: https://docs.pyrogram.org/start/auth'
        == response.json()['SESSION_ERROR']
    )


@pytest.mark.anyio
async def test_route_envio_com_inexistente_session(client: AsyncClient):
    response = await client.get('/teste-envio/inexistente')
    assert response.status_code == 200
    assert 'SESSION FILE DOESNT EXISTS' == response.json()['SESSION_ERROR']


@pytest.mark.anyio
async def test_route_listar_chats(client: AsyncClient):
    response = await client.post(
        '/listar-chats', json={'session_file': 'valid'}
    )
    assert response.status_code == 200
    assert 'Me andme' in response.json().keys()


@pytest.mark.anyio
async def test_route_listar_chats_com_inexistente_session(client: AsyncClient):
    response = await client.post(
        '/listar-chats', json={'session_file': 'inexistente'}
    )
    assert response.status_code == 200
    assert 'SESSION FILE DOESNT EXISTS' == response.json()['SESSION_ERROR']


@pytest.mark.anyio
async def test_route_listar_chats_com_invalid_session(client: AsyncClient):
    response = await client.post(
        '/listar-chats', json={'session_file': 'invalid'}
    )
    assert response.status_code == 200
    assert (
        'The API key is required for new authorizations. More info: https://docs.pyrogram.org/start/auth'
        == response.json()['SESSION_ERROR']
    )


@pytest.mark.anyio
async def test_route_enviar_msg(client: AsyncClient):
    global msg_to_delete1
    response = await client.post(
        '/enviar', json={'session_file': 'valid', 'chat_id': 'me'}
    )
    msg_to_delete1 = response.json()['id']
    assert (
        'id' in response.json().keys()
        and 'date' in response.json().keys()
        and 'text' in response.json().keys()
    )


@pytest.mark.anyio
async def test_route_enviar_msg_com_inexistente_session(client: AsyncClient):
    response = await client.post(
        '/enviar', json={'session_file': 'valid2', 'chat_id': 'me'}
    )
    assert 'SESSION FILE DOESNT EXISTS' == response.json()['SESSION_ERROR']


@pytest.mark.anyio
async def test_route_enviar_msg_com_invalid_session(client: AsyncClient):
    response = await client.post(
        '/enviar', json={'session_file': 'invalid', 'chat_id': 'me'}
    )
    assert (
        'The API key is required for new authorizations. More info: https://docs.pyrogram.org/start/auth'
        == response.json()['SESSION_ERROR']
    )


@pytest.mark.anyio
async def test_route_responder_msg(client: AsyncClient):
    global msg_to_delete2
    response = await client.post(
        '/responder',
        json={
            'session_file': 'valid',
            'chat_id': 'me',
            'message_id': msg_to_delete1,  # to reply
            'message_text': 'reply',
        },
    )
    msg_to_delete2 = response.json()['id']
    assert (
        'id' in response.json().keys()
        and 'date' in response.json().keys()
        and 'text' in response.json().keys()
    )


@pytest.mark.anyio
async def test_route_responder_msg_com_inexistente_session(
    client: AsyncClient,
):
    response = await client.post(
        '/responder',
        json={
            'session_file': 'valid1321',
            'chat_id': 'me',
            'message_id': msg_to_delete1,  # to reply
            'message_text': 'reply',
        },
    )
    assert 'SESSION FILE DOESNT EXISTS' == response.json()['SESSION_ERROR']


@pytest.mark.anyio
async def test_route_responder_msg_com_invalid_session(client: AsyncClient):
    response = await client.post(
        '/responder',
        json={
            'session_file': 'invalid',
            'chat_id': 'me',
            'message_id': msg_to_delete1,  # to reply
            'message_text': 'reply',
        },
    )
    assert (
        'The API key is required for new authorizations. More info: https://docs.pyrogram.org/start/auth'
        == response.json()['SESSION_ERROR']
    )


@pytest.mark.anyio
async def test_route_deletar_msg_com_inexistente_session(client: AsyncClient):
    response = await client.post(
        '/deletar',
        json={
            'session_file': 'valid123',
            'chat_id': 'me',
            'message_id': msg_to_delete1,
        },
    )
    assert 'SESSION FILE DOESNT EXISTS' == response.json()['SESSION_ERROR']


@pytest.mark.anyio
async def test_route_deletar_msg_com_invalid_session(client: AsyncClient):
    response = await client.post(
        '/deletar',
        json={
            'session_file': 'invalid',
            'chat_id': 'me',
            'message_id': msg_to_delete1,
        },
    )
    assert (
        'The API key is required for new authorizations. More info: https://docs.pyrogram.org/start/auth'
        == response.json()['SESSION_ERROR']
    )


@pytest.mark.anyio
async def test_route_deletar_msg_com_invalid_session(client: AsyncClient):
    response = await client.post(
        '/deletar',
        json={
            'session_file': 'invalid',
            'chat_id': 'me',
            'message_id': msg_to_delete1,
        },
    )
    assert (
        'The API key is required for new authorizations. More info: https://docs.pyrogram.org/start/auth'
        == response.json()['SESSION_ERROR']
    )


@pytest.mark.anyio
async def test_route_deletar_msg(client: AsyncClient):
    response_del1 = await client.post(
        '/deletar',
        json={
            'session_file': 'valid',
            'chat_id': 'me',
            'message_id': msg_to_delete1,
        },
    )
    response_del2 = await client.post(
        '/deletar',
        json={
            'session_file': 'valid',
            'chat_id': 'me',
            'message_id': msg_to_delete2,
        },
    )
    assert (
        response_del1.json()['SUCCESS'] == 1
        and response_del2.json()['SUCCESS'] == 1
    )
