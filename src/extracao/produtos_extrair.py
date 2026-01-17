import requests
import pandas as pd
from datetime import date
from sqlalchemy import create_engine

url = "https://dummyjson.com/products"
response = requests.get(url)

data = response.json()
produtos = data["products"]

df = pd.DataFrame(produtos)

# PRODUTOS
df_produtos = df[
    ["id", "sku", "title", "brand", "category", "price"]
].rename(columns={
    "id": "produto_id",
    "title": "nome_produto",
    "brand": "marca",
    "category": "categoria",
    "price": "preco"
})

engine = create_engine(
    "mssql+pyodbc://@PC-JOW/dados_ecommerce?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

ids_existentes = pd.read_sql(
    "SELECT produto_id FROM produtos",
    engine
)

df_produtos_novos = df_produtos[
    ~df_produtos["produto_id"].isin(ids_existentes["produto_id"])
]

if not df_produtos_novos.empty:
    df_produtos_novos.to_sql(
        "produtos",
        engine,
        if_exists="append",
        index=False
    )
    print(f"{len(df_produtos_novos)} novos produtos inseridos.")
else:
    print("Nenhum produto novo para inserir.")

# ESTOQUE
df_estoque_atual = (
    df[["id","stock"]]
    .rename(columns={
        "id":"produto_id",
        "stock":"quantidade"
    })
)

df_estoque_atual["estoque_id"] = 1
df_estoque_atual["data_referencia"] = date.today()

ids_existentes_estoque = pd.read_sql(
    """
    SELECT produto_id 
    FROM estoque_atual
    WHERE estoque_id = 1
    """,
    engine
)

df_estoque_atual_novos = df_estoque_atual[
    ~df_estoque_atual["produto_id"].isin(ids_existentes_estoque["produto_id"])
]

if not df_estoque_atual_novos.empty:
    df_estoque_atual_novos.to_sql(
        "estoque_atual",
        engine,
        if_exists="append",
        index=False
    )
    print(f"{len(df_estoque_atual_novos)} novos produtos inseridos no estoque.")
else:
    print("Nenhum produto novo para inserir.")
