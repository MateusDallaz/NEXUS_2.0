from database             import SessionLocal
from class_convite        import Convite
from class_usuario        import Usuario
from class_categoriaCanal import Categoria
from class_servidor       import Servidor
from class_canal          import Canal

session = SessionLocal()

novo_convite = Convite(
    guilda_serv     = "3",
    sala_canal      = "1",
    apelido_criador = "1",
    codigo          = "T3ST3",
    usos_max        = None,
    usos_atual      = "0",
    data_expiracao  = None
)

session.add(novo_convite)
session.commit()
print("Convite criado com sucesso")

session.close()
