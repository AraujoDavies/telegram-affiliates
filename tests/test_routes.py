import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_healthecheck(client: AsyncClient):
    response = await client.get('/healthcheck')
    assert response.json() == {'healthcheck': 'OK'}


@pytest.mark.anyio
async def test_route_teste_envio(client: AsyncClient):
    response = await client.get('/teste-envio/me')
    assert response.status_code == 200
    assert (
        'Oi, teste efetuado com sucesso atráves da API-AFFILIATES'
        == response.json()['text']
    )


@pytest.mark.anyio
async def test_route_listar_chats(client: AsyncClient):
    response = await client.post('/listar-chats')
    assert response.status_code == 200
    assert 'Me andme' in response.json().keys()
