from sqlalchemy import Column, Integer, String, ForeignKey
from database   import Base

class Cargo(Base):
    __tablename__ = "cargo"

    patente     = Column(Integer, primary_key=True)
    guilda_serv = Column(Integer, ForeignKey("servidor.guilda"), nullable=False)
    nome        = Column(String, nullable=False)
    permissoes  = Column(Integer, nullable=False)
