from urllib import response

import pytest
from httpx import AsyncClient

# @pytest.mark.anyio
# async def test_healthecheck(client: AsyncClient):
#     response = await client.get('/healthcheck')
#     assert response.json() == {'healthcheck': 'OK'}


# @pytest.mark.anyio
# async def test_route_teste_envio(client: AsyncClient):
#     response = await client.get('/teste-envio/me/valid')
#     assert response.status_code == 200
#     assert (
#         'Oi, teste efetuado com sucesso atráves da API-AFFILIATES'
#         == response.json()['text']
#     )


# @pytest.mark.anyio
# async def test_route_listar_chats(client: AsyncClient):
#     response = await client.post('/listar-chats', json={"session_file": "valid"})
#     assert response.status_code == 200
#     assert 'Me andme' in response.json().keys()


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
async def test_route_responder_msg(client: AsyncClient):
    global msg_to_delete2
    response = await client.post(
        '/responder',
        json={
            'session_file': 'valid',
            'chat_id': 'me',
            'message_id': msg_to_delete1,
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
