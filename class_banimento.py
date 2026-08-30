from sqlalchemy     import Column, Integer, String, Date, ForeignKey
from sqlalchemy.sql import func
from database       import Base

class Banimento(Base):
    __tablename__ = "banimento"

    veto            = Column(Integer, primary_key=True)
    guilda_serv     = Column(Integer, ForeignKey("servidor.guilda"), nullable=False)
    apelido_banido  = Column(Integer, ForeignKey("usuario.apelido"), nullable=False)
    apelido_banidor = Column(Integer, ForeignKey("usuario.apelido"), nullable=True)
    motivo          = Column(String, nullable=True)
    data_banimento  = Column(Date, nullable=False, server_default=func.current_timestamp())
