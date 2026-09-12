from database       import SessionLocal
from class_servidor import Servidor
from class_usuario  import Usuario

session = SessionLocal()

novo_servidor = Servidor(
    nome         = "Servidor Teste 1",
    apelido_dono = "1"
)

session.add(novo_servidor)
session.commit()
print("Servidor criado com sucesso")

session.close()
