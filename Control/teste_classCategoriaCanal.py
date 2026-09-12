from database             import SessionLocal
from class_categoriaCanal import Categoria
from class_servidor       import Servidor

session = SessionLocal()

nova_categoria = Categoria(
    guilda_serv = "3",
    nome = "Teste"
)

session.add(nova_categoria)
session.commit()
print("Nova Categoria Criada com Sucesso")

session.close()