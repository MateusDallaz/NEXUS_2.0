from database import SessionLocal
from class_cargo import Cargo
from class_servidor import Servidor

session = SessionLocal()

novo_cargo = Cargo(
    guilda_serv = "3",
    nome = "Teste",
    permissoes = "1"
)

session.add(novo_cargo)
session.commit()
print("Novo Cargo Inserido com Sucesso")

session.close()