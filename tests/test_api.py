import json


def test_retorno_de_todos_os_clientes_status_code_200(api_client):
    response = api_client.get("/cliente/")
    assert response.status_code == 200


def test_retorno_de_todos_os_clientes_e_uma_lista(api_client):
    response = api_client.get("/cliente/")
    assert response.json() == []


def test_retorno_de_um_cliente_nao_cadastrado_status_code_404(api_client):
    response = api_client.get("/cliente/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Cliente não encontrado."}


def test_retorno_de_um_cliente_status_code_200(api_client, api_cliente_test):
    response = api_client.get(f"/cliente/{api_cliente_test.id}")
    assert response.status_code == 200


def test_criar_um_cliente_com_retorno_status_code_201(api_client):
    request_data = json.dumps({
        "username": "Aryanne",
        "email": "aryanne@test.com",
        "phone": "81911111122"
    })
    response = api_client.post("/cliente/", json=json.loads(request_data))
    assert response.status_code == 201
    assert response.json()["username"] == "Aryanne"
    assert response.json()["email"] == "aryanne@test.com"
    assert response.json()["phone"] == "81911111122"


def test_atualizar_campos_de_um_cliente_cadastrado_status_code_204(api_client):
    data_request = json.dumps({
        "username": "Aryanne Ferreira",
        "email": "aryanneferr@test.com",
        "phone": "81977774444"
    })
    response = api_client.put("/cliente/2", json=json.loads(data_request))
    assert response.status_code == 204


def test_excluir_um_cliente_cadastrado_status_code_204(api_client):
    response = api_client.delete("/cliente/1")
    assert response.status_code == 204


