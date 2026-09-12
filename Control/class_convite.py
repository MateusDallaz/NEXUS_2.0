from sqlalchemy     import Column, Integer, String, ForeignKey, Date
from sqlalchemy.sql import func
from database       import Base

class Convite(Base):
    __tablename__ = "convite"

    passe           = Column(Integer, primary_key=True)
    guilda_serv     = Column(Integer, ForeignKey("servidor.guilda"), nullable=False)
    sala_canal      = Column(Integer, ForeignKey("canal.sala"), nullable=False)
    apelido_criador = Column(Integer, ForeignKey("usuario.apelido"), nullable=False)
    codigo          = Column(String, nullable=False)
    usos_max        = Column(Integer, nullable=True)
    usos_atual      = Column(Integer, nullable=False)
    data_expiracao  = Column(Date, nullable=True)
    data_criacao    = Column(Date, nullable=False, server_default=func.current_timestamp())