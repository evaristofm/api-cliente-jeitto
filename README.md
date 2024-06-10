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
$ docker compose exec api app alembic upgrade head

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

Comandos CLI que podem ser úteis

o comando abaixo lsita todos os comandos cadastrados no projeto:

```
docker compose exec api app --help

```

![lista_help_comandos](https://github.com/evaristofm/api-cliente-jeitto/assets/46290279/2806b3ad-0538-4aaa-a2ef-60540ec9a354)


o seguinte comando lista todos os clientes cadastrados no banco de dados:

```
docker compose exec api app cliente-list

```
![lista_clientes_cli](https://github.com/evaristofm/api-cliente-jeitto/assets/46290279/74651d3f-baf3-4ce2-bfd2-7d7742df524c)


o próximo comando podemos criar um cliente via linha de comando.
Segue um exemplo:

```
docker compose exec api app cliente-create "John Doe" jhondoe@test.com 81977777777

```
![criar_cliente_cli](https://github.com/evaristofm/api-cliente-jeitto/assets/46290279/43f7e801-9014-451b-bc19-dd044744ec69)

![lista_cliente_2_cli](https://github.com/evaristofm/api-cliente-jeitto/assets/46290279/a8b86732-e1a2-4884-8950-e90742fb8151)

