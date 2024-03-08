import sqlalchemy
import uuid

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from Insert_NF import Inserir_nf, Insert
from BD import *
from Classes import clientes_bot

#CRIAÇÃO DA PRIMEIRA STRING BD_ROBOT
# SQL Alchemy é a ponte do código para o BANCO
engine = sqlalchemy.create_engine('mssql+pyodbc://rafael.rocha:Certa%402024@192.168.0.26/Teste_CertaBot?driver=ODBC+Driver+17+for+SQL+Server', echo=True)

# Função base para código em Tabela
Base = declarative_base()

# Pego o argumento BASE da classe 'clientes_bot' e faço a criação da tabela
Base.metadata.create_all(engine)

# Cria a sessão do Banco de Dados
Sessao = sessionmaker(bind=engine)
session = Sessao()


#CRIAÇÃO DA SEGUNDA STRING BD_CLIENTE
engine2 = sqlalchemy.create_engine('mssql')
Base2 = declarative_base()
Base2.metadata.creat_all(engine2)
