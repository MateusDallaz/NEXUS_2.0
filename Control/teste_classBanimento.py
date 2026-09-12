from database        import SessionLocal
from class_banimento import Banimento
from class_servidor  import Servidor
from class_usuario   import Usuario

session = SessionLocal()

novo_banimento = Banimento(
    guilda_serv     = "3",
    apelido_banido  = "2",
    apelido_banidor = "1",
    motivo          = "Teste"
)

session.add(novo_banimento)
session.commit()
print("Banimento criado com sucesso")

session.close()
