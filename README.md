# Mock Cliente API


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- [x] Acesso a um computador com Python -> (Python 3.11.7)
- [x] Terminal Linux/Mac (ou WSL)
- [x] Docker e docker compose -> (Docker version 26.1.3) - (Docker Compose version v2.27.1)


## 🚀 Instalando API Cliente

```
$ cd pasta/onde/vc/guarda/seus/projetos
$ git https://github.com/evaristofm/api-cliente-jeitto.git

```
próximo passo: no diretorio raiz do repositório executar:

```
$ docker compose up -d --build

```
próximo passo: execute as migrações do projeto usando docker compose + alembic

```
$ docker compose exec api prev alembic upgrade head

```

Cobertura de testes (ambiente linux)

```
$ ./tests.sh

```
![tests](https://github.com/evaristofm/api-cliente-jeitto/assets/46290279/86292786-30be-4020-aa7a-ae59b6ee9764)


Conexão com o banco de dados Postgres

```
POSTGRES_DB=app || POSTGRES_DB=app_test
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
PORT=5435

```

Acessando a documentação SWAGGER da API

```
http://localhost:8000/docs

```

![swagger](https://github.com/evaristofm/api-cliente-jeitto/assets/46290279/4595ac9d-2e7f-4552-a0c6-b74f64256244)



