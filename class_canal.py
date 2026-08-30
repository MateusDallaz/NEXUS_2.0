from sqlalchemy import Column, Integer, String, ForeignKey
from database   import Base

class Canal(Base):
    __tablename__ = "canal"

    sala        = Column(Integer, primary_key=True)
    guilda_serv = Column(Integer, ForeignKey("servidor.guilda"), nullable=False)
    secao_canal = Column(Integer, ForeignKey("categoria_canal.secao"), nullable=False)
    nome        = Column(String, nullable=False)
    tipo        = Column(String, nullable=False)