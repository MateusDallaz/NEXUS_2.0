from sqlalchemy     import Column, Integer, String, Date
from sqlalchemy.sql import func
from database       import Base

class Usuario(Base):
    __tablename__ = "usuario"

    apelido      = Column(Integer, primary_key=True)
    nome_usuario = Column(String, nullable=False)
    email        = Column(String, nullable=False)
    senha        = Column(String, nullable=False)
    status_serv  = Column(String, nullable=False)
    data_criacao = Column(Date, nullable=False,server_default=func.current_timestamp())