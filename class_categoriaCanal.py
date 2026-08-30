from sqlalchemy import Column, Integer, String, ForeignKey
from database   import Base

class Categoria(Base):
    __tablename__ = "categoria_canal"

    secao       = Column(Integer, primary_key=True)
    guilda_serv = Column(Integer, ForeignKey("servidor.guilda"), nullable=False)
    nome        = Column(String, nullable=False)