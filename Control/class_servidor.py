from sqlalchemy     import Column, Integer, String, Date, ForeignKey
from sqlalchemy.sql import func
from database       import Base

class Servidor(Base):
    __tablename__ = "servidor"

    guilda       = Column(Integer, primary_key=True)
    nome         = Column(String, nullable=False)
    apelido_dono = Column(Integer, ForeignKey("usuario.apelido"), nullable=False)
    data_criacao = Column(Date, nullable=False, server_default=func.current_timestamp())