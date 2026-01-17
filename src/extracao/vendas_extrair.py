import requests
import pandas as pd
from datetime import date
from sqlalchemy import create_engine


vendas_url = "https://dummyjson.com/carts"
resposta = requests.get(vendas_url)

carrinho = resposta.json()
vendas = carrinho["carts"]


df_vendas = pd.DataFrame(vendas)

print(df_vendas)