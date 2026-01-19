# Análise de Estoque – E-commerce (DummyJSON)

Este projeto tem como objetivo simular um fluxo de ingestão e análise de dados de um e-commerce,
utilizando dados públicos da API DummyJSON.

Os dados de produtos são extraídos via API, tratados em Python com a biblioteca Pandas
e armazenados em um banco de dados SQL Server por meio da biblioteca SQLAlchemy.

O foco do projeto é demonstrar conceitos de:

- Extração de dados via API
- Tratamento e padronização de dados
- Modelagem de dados em banco relacional
- Integração com ferramentas de análise (Power BI)

Este projeto **não tem como objetivo reproduzir um sistema transacional real**,
mas sim servir como um **estudo prático de engenharia e análise de dados**.

---

## Tecnologias Utilizadas

- **Python**
  - Pandas – limpeza, transformação e padronização dos dados
  - Requests – consumo de dados via API REST
  - SQLAlchemy – conexão e persistência dos dados no SQL Server

- **SQL Server**
  - Armazenamento dos dados em banco relacional
  - Modelagem das tabelas de produtos e estoque

- **Power BI**
  - Criação de dashboards e análises visuais

- **Git & GitHub**
  - Versionamento e organização do projeto

---

##  Modelagem do Banco de Dados

O banco de dados foi modelado de forma relacional para simular um cenário de e-commerce:

- A tabela **produtos** armazena o cadastro base dos itens.
- A tabela **estoques** define os tipos de estoque existentes.
- A tabela **estoque_atual** registra o histórico diário de quantidade por produto e estoque.
- Foi utilizada **chave primária composta** para permitir análise temporal.
- As tabelas se relacionam por **chaves estrangeiras**, evitando duplicidade de dados.

Essa modelagem permite análises históricas e integração direta com o Power BI.

---

## Próximos Passos

- Criar uma tabela de vendas a partir da API de carrinhos (`/carts`), desmembrando produtos por linha.
- Implementar uma tabela de movimentação de estoque (entradas e saídas).
- Utilizar os dados de vendas para impactar o estoque de forma analítica.
- Desenvolver dashboards no Power BI para análise de produtos, estoque e vendas.
- Evoluir o projeto com foco em **análise de dados e tomada de decisão**, não operação.
