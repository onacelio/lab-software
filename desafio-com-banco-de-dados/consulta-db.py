import pyodbc as bd
import pandas as pd

dados_conexao = ("Driver={SQL Server};"
                 "Server=DESKTOP-4E80G57;"
                 "Database=ContosoRetailDW")

conexao = bd.connect(dados_conexao)
print("Conexão bem sucedida")

vendas_df = pd.read_sql("SELECT * FROM ContosoRetailDW.dbo.FactSales", conexao)
print(vendas_df)
