from database      import SessionLocal
from class_usuario import Usuario

session = SessionLocal()

novo_usuario = Usuario(
    nome_usuario = "Teste 2",
    email        = "teste@teste2.com",
    senha        = "123456",
    status_serv  = "Online"
)

session.add(novo_usuario)
session.commit()
print("Usuario inserido com sucesso")

session.close()