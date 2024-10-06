🌾 Farm Producer Management API

API para gerenciamento de produtores rurais, construída com FastAPI e PostgreSQL. A API permite cadastrar, editar e excluir produtores, além de fornecer dados para um dashboard sobre fazendas cadastradas.

🛠 Tecnologias Utilizadas

	•	FastAPI - Framework para desenvolvimento da API.
	•	PostgreSQL - Banco de dados relacional.
	•	SQLAlchemy - ORM para integração com o banco de dados.
	•	Docker - Containerização da aplicação.
	•	pytest - Testes unitários.

🚀 Como Subir o Projeto

Pré-requisitos

	•	Docker e Docker Compose instalados na sua máquina.

Passos

	1.	Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


	2.	Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:

DATABASE_URL=postgresql://user:password@db/producers_db
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=producers_db


	3.	Suba os containers com Docker Compose:

docker-compose up --build

Isso vai inicializar a API na porta 8000 e o banco de dados PostgreSQL na porta 5432.

	4.	Acesse a documentação da API:
	•	Swagger UI: http://localhost:8000/docs
	•	OpenAPI JSON: http://localhost:8000/openapi.json

📄 Rotas da API

1. Health Check

	•	GET /health
	•	Descrição: Verifica se a API está funcionando corretamente.
	•	Exemplo de resposta:

{
  "status": "OK"
}



2. Cadastrar Produtor

	•	POST /producers/
	•	Descrição: Cadastra um novo produtor rural.
	•	Corpo da Requisição:

{
  "cpf_cnpj": "12345678901",
  "name": "John Doe",
  "farm_name": "Green Farm",
  "city": "Rural City",
  "state": "MG",
  "total_area": 100.0,
  "agricultural_area": 60.0,
  "vegetation_area": 40.0,
  "crops": ["Soybean", "Corn"]
}


	•	Exemplo de resposta:

{
  "id": 1,
  "cpf_cnpj": "12345678901",
  "name": "John Doe",
  "farm_name": "Green Farm",
  "city": "Rural City",
  "state": "MG",
  "total_area": 100.0,
  "agricultural_area": 60.0,
  "vegetation_area": 40.0,
  "crops": ["Soybean", "Corn"]
}



3. Listar Produtores

	•	GET /producers/
	•	Descrição: Lista todos os produtores cadastrados.
	•	Exemplo de resposta:

[
  {
    "id": 1,
    "cpf_cnpj": "12345678901",
    "name": "John Doe",
    "farm_name": "Green Farm",
    "city": "Rural City",
    "state": "MG",
    "total_area": 100.0,
    "agricultural_area": 60.0,
    "vegetation_area": 40.0,
    "crops": ["Soybean", "Corn"]
  }
]



4. Remover Produtor

	•	DELETE /producers/{producer_id}
	•	Descrição: Remove um produtor pelo ID.
	•	Exemplo de resposta:

{
  "message": "Producer successfully removed"
}



📊 Dados do Dashboard

1. Total de Fazendas e Área Total

	•	GET /dashboard/totals
	•	Descrição: Retorna o número total de fazendas e a soma da área total.
	•	Exemplo de resposta:

{
  "total_farms": 10,
  "total_area": 5000
}



2. Distribuição por Estado

	•	GET /dashboard/state-distribution
	•	Descrição: Retorna a distribuição das fazendas por estado.
	•	Exemplo de resposta:

[
  {
    "state": "MG",
    "total_farms": 5
  },
  {
    "state": "SP",
    "total_farms": 3
  }
]



3. Distribuição por Cultura

	•	GET /dashboard/crop-distribution
	•	Descrição: Retorna a distribuição de culturas plantadas nas fazendas.
	•	Exemplo de resposta:

[
  {
    "crop": "Soybean",
    "total_farms": 4
  },
  {
    "crop": "Corn",
    "total_farms": 3
  }
]



4. Distribuição de Uso de Solo

	•	GET /dashboard/land-use
	•	Descrição: Retorna a distribuição de áreas agricultáveis e vegetação.
	•	Exemplo de resposta:

{
  "total_agricultural_area": 3000,
  "total_vegetation_area": 2000
}


🧪 Executando Testes

Para rodar os testes unitários, execute o seguinte comando:

docker exec -it serasa-web-1 pytest

Isso executa os testes dentro do container web.


📦 Camadas de Projeto
```
Serasa
├─ .env
├─ .env.example
├─ Dockerfile
├─ README.md
├─ app
│  ├─ api
│  │  └─ v1
│  │     ├─ controllers
│  │     │  └─ producer_controller.py
│  │     ├─ routes
│  │     │  ├─ dashboard.py
│  │     │  └─ producer.py
│  │     └─ schemas
│  │        └─ producer.py
│  ├─ core
│  │  └─ config.py
│  ├─ db
│  │  └─ database.py
│  ├─ main.py
│  ├─ models
│  │  ├─ __init__.py
│  │  └─ producer.py
│  ├─ services
│  │  └─ producer_service.py
│  └─ tests
│     ├─ test_producer_controller.py
│     └─ test_producer_routes.py
├─ docker-compose.yml
└─ requirements.txt

```