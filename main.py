from fastapi                 import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses       import FileResponse
from database                import SessionLocal
from class_usuario           import Usuario
from class_servidor          import Servidor
from class_membro            import Membro
from class_cargo             import Cargo
from class_categoriaCanal    import Categoria
from class_canal             import Canal
from class_convite           import Convite
from class_banimento         import Banimento

app = FastAPI()

@app.get("/")
def index():
    return FileResponse("index.html")

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/usuario")
def lista_usuario():

    session = SessionLocal()
    usuarios = session.query(Usuario).all()
    resultado = [{"Apelido": u.apelido, 
                  "Nome de Usuário": u.nome_usuario, 
                  "E-mail": u.email, 
                  "Senha": u.senha, 
                  "Status do Usuário": u.status_serv, 
                  "Data de Criação": u.data_criacao}
                 for u in usuarios]
    session.close()
    return resultado

@app.get("/servidor")
def lisa_servidor():

    session = SessionLocal()
    servidores = session.query(Servidor).all()
    resultado = [{"Guilda": u.guilda, 
                  "Nome do Servidor": u.nome, 
                  "Apelido do Dono": u.apelido_dono, 
                  "Data de Criação": u.data_criacao}
                 for u in servidores]
    session.close()
    return resultado

@app.get("/membro")
def lista_membro():

    session = SessionLocal()
    membros = session.query(Membro).all()
    resultado = [{"Cracha": u.cracha, 
                  "Apelido de Usuário": u.apelido_usuario, 
                  "Guilda do Servidor": u.guilda_serv, 
                  "Nome": u.nome, 
                  "Apelido no Servidor": u.apelido_no_servidor, 
                  "Data de Entrada": u.data_entrada}
                 for u in membros]
    session.close()
    return resultado

@app.get("/cargo")
def lista_cargo():

    session = SessionLocal()
    cargos = session.query(Cargo).all()
    resultado = [{"Patente": u.patente, 
                  "Guilda do Servidor": u.guilda_serv, 
                  "Nome do Cargo": u.nome, 
                  "Permissões": u.permissoes}
                 for u in cargos]
    session.close()
    return resultado

@app.get("/categoria_canal")
def lista_categoria():

    session = SessionLocal()
    categorias = session.query(Categoria).all()
    resultado = [{"Seção": u.secao,
                "Guilda do Servidor": u.guilda_serv,
                "Nome da Categoria": u.nome}
                for u in categorias]
    session.close()
    return resultado

@app.get("/canal")
def lista_canal():

    session = SessionLocal()
    canais = session.query(Canal).all()
    resultado = [{"Sala": u.sala,
                  "Guilda do Servidor": u.guilda_serv,
                  "Seção de Categoria": u.secao_canal,
                  "Nome do Canal": u.nome,
                  "Tipo de Canal": u.tipo}
                  for u in canais]
    session.close()
    return resultado

@app.get("/convite")
def lista_convite():

    session = SessionLocal()
    convites = session.query(Convite).all()
    resultado = [{"Passe": u.passe,
                  "Guilda do Servidor": u.guilda_serv,
                  "Sala do Canal": u.sala_canal,
                  "Apelido do Criador": u.apelido_criador,
                  "Código": u.codigo,
                  "Usos Máximos": u.usos_max,
                  "Usos Atuais": u.usos_atual,
                  "Data de Expiração": u.data_expiracao,
                  "Data de Criação": u.data_criacao}
                  for u in convites]
    session.close()
    return resultado

@app.get("/banimento")
def lista_banimento():

    session = SessionLocal()
    banimentos = session.query(Banimento).all()
    resultado = [{"Veto": u.veto,
                  "Guilda do Servidor": u.guilda_serv,
                  "Apelido do Banido": u.apelido_banido,
                  "Apelido do Banidor": u.apelido_banidor,
                  "Motivo": u.motivo,
                  "Data de Banimento": u.data_banimento}
                  for u in banimentos]
    session.close()
    return resultado
