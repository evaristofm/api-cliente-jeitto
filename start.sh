#!/usr/bin/bash

# Arquivos na raiz
touch setup.py
touch {pyproject,settings,.secrets}.toml
touch {requirements,MANIFEST}.in
touch Dockerfile.dev docker-compose.yaml

# Imagem do banco de dados
mkdir postgres
touch postgres/{Dockerfile,create-databases.sh}

# Aplicação
mkdir -p app/{models,routes}
touch app/default.toml
touch app/{__init__,cli,app,db,security,config}.py
touch app/models/{__init__}.py
touch app/routes/{__init__}.py

# Testes
touch test.sh
mkdir tests
touch tests/{__init__,conftest,test_api}.py