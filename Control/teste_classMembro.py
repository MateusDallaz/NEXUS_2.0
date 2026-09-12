from database       import SessionLocal
from class_membro   import Membro
from class_servidor import Servidor
from class_usuario  import Usuario

session = SessionLocal()

novo_membro = Membro(
    apelido_usuario     = "1",
    guilda_serv         = "3",
    nome                = "Teste",
    apelido_no_servidor = "Testando"
)

session.add(novo_membro)
session.commit()
print("Membro adicionado com Sucesso")

session.close()