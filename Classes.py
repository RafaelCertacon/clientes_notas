# Criação da tabela com seus valores/atributos. Em formato de Código PYTHON
class clientes_bot(Base):
    __tablename__ = 'clientes_bot'
    ID_CLIENTE = Column(String(250), primary_key=True, default=str(uuid.uuid4()), autoincrement=True)
    NOME = Column(String(100))
    CNPJ_CPF = Column(String(20))
    TIPO_ARQUIVO = Column(String(20))
    STATUS = Column(String(15))


class tabela_faltantes():
    __tablename__ = 'clientes_bot'
    ID_CLIENTE = Column(String(250), primary_key=True, default=str(uuid.uuid4()), autoincrement=True)
