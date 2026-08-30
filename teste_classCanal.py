from database             import SessionLocal
from class_canal          import Canal
from class_categoriaCanal import Categoria
from class_servidor       import Servidor

session = SessionLocal()

novo_canal = Canal(
    guilda_serv = "3",
    secao_canal = "1",
    nome = "Teste",
    tipo = "voz"
)

session.add(novo_canal)
session.commit()
print("Novo Canal Criado com Sucesso")

session.close()