from sqlalchemy     import Column, Integer, String, Date, ForeignKey
from sqlalchemy.sql import func
from database       import Base

class Membro(Base):
    __tablename__ = "membro"

    cracha              = Column(Integer, primary_key=True)
    apelido_usuario     = Column(Integer, ForeignKey("usuario.apelido"), nullable=False)
    guilda_serv         = Column(Integer, ForeignKey("servidor.guilda"), nullable=False)
    nome                = Column(String, nullable=False)
    apelido_no_servidor = Column(String, nullable=False)
    data_entrada        = Column(Date, nullable=False, server_default=func.current_timestamp())