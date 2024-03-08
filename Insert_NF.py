import pandas as pd

from BD import clientes_bot, Insert

def Inserir_nf():
    pegar_nf = pd.read_csv('./Nota_Fiscal/Arquivo_csv.csv')
    print(pegar_nf)

    if clientes_bot == pegar_nf:
       novo_upload = clientes_bot(
           ID_CLIENTE=primary_key.decode("utf-8"),
           NOME= nome_cliente,
           CNPJ_CPF=cnpj_cpf,
           TIPO_ARQUIVO=None,
           STATUS=None
       )
    else:
        print("Erro ao inserir no banco de dados")

    session.add(novo_upload)
    session.commit()


def Insert(clientes_bot):
    session.add(clientes_bot)
    session.commit()