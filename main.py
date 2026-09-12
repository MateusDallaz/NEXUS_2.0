import sys
from pathlib                 import Path
from datetime                import date

sys.path.insert(0, str(Path(__file__).parent / "Control"))

from fastapi                 import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses       import FileResponse
from pydantic                import BaseModel, ConfigDict, Field
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
    return FileResponse("View/index.html")

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class UsuarioEntrada(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    nome_usuario: str = Field(alias="Nome de Usuário")
    email:        str = Field(alias="E-mail")
    senha:        str = Field(alias="Senha")
    status_serv:  str = Field(alias="Status do Usuário")

class ServidorEntrada(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    nome:         str = Field(alias="Nome do Servidor")
    apelido_dono: int = Field(alias="Apelido do Dono")

class MembroEntrada(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    apelido_usuario:     int = Field(alias="Apelido de Usuário")
    guilda_serv:         int = Field(alias="Guilda do Servidor")
    nome:                str = Field(alias="Nome")
    apelido_no_servidor: str = Field(alias="Apelido no Servidor")

class CargoEntrada(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    guilda_serv: int = Field(alias="Guilda do Servidor")
    nome:        str = Field(alias="Nome do Cargo")
    permissoes:  int = Field(alias="Permissões")

class CategoriaEntrada(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    guilda_serv: int = Field(alias="Guilda do Servidor")
    nome:        str = Field(alias="Nome da Categoria")

class CanalEntrada(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    guilda_serv: int = Field(alias="Guilda do Servidor")
    secao_canal: int = Field(alias="Seção de Categoria")
    nome:        str = Field(alias="Nome do Canal")
    tipo:        str = Field(alias="Tipo de Canal")

class ConviteEntrada(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    guilda_serv:     int = Field(alias="Guilda do Servidor")
    sala_canal:      int = Field(alias="Sala do Canal")
    apelido_criador: int = Field(alias="Apelido do Criador")
    codigo:          str = Field(alias="Código")
    usos_max:        int | None = Field(default=None, alias="Usos Máximos")
    usos_atual:      int = Field(alias="Usos Atuais")
    data_expiracao:  date | None = Field(default=None, alias="Data de Expiração")

class BanimentoEntrada(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    guilda_serv:     int = Field(alias="Guilda do Servidor")
    apelido_banido:  int = Field(alias="Apelido do Banido")
    apelido_banidor: int | None = Field(default=None, alias="Apelido do Banidor")
    motivo:          str | None = Field(default=None, alias="Motivo")

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

@app.post("/usuario")
def criar_usuario(dados: UsuarioEntrada):

    session = SessionLocal()
    session.add(Usuario(**dados.model_dump(by_alias=False)))
    session.commit()
    session.close()
    return {"mensagem": "Usuário criado com sucesso"}

@app.put("/usuario/{apelido}")
def alterar_usuario(apelido: int, dados: UsuarioEntrada):

    session = SessionLocal()
    usuario = session.query(Usuario).filter(Usuario.apelido == apelido).first()
    if usuario is None:
        session.close()
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    for campo, valor in dados.model_dump(by_alias=False).items():
        setattr(usuario, campo, valor)

    session.commit()
    session.close()
    return {"mensagem": "Usuário alterado com sucesso"}

@app.delete("/usuario/{apelido}")
def excluir_usuario(apelido: int):

    session = SessionLocal()
    usuario = session.query(Usuario).filter(Usuario.apelido == apelido).first()
    if usuario is None:
        session.close()
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    session.delete(usuario)
    session.commit()
    session.close()
    return {"mensagem": "Usuário excluído com sucesso"}

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

@app.post("/servidor")
def criar_servidor(dados: ServidorEntrada):

    session = SessionLocal()
    session.add(Servidor(**dados.model_dump(by_alias=False)))
    session.commit()
    session.close()
    return {"mensagem": "Servidor criado com sucesso"}

@app.put("/servidor/{guilda}")
def alterar_servidor(guilda: int, dados: ServidorEntrada):

    session = SessionLocal()
    servidor = session.query(Servidor).filter(Servidor.guilda == guilda).first()
    if servidor is None:
        session.close()
        raise HTTPException(status_code=404, detail="Servidor não encontrado")

    for campo, valor in dados.model_dump(by_alias=False).items():
        setattr(servidor, campo, valor)

    session.commit()
    session.close()
    return {"mensagem": "Servidor alterado com sucesso"}

@app.delete("/servidor/{guilda}")
def excluir_servidor(guilda: int):

    session = SessionLocal()
    servidor = session.query(Servidor).filter(Servidor.guilda == guilda).first()
    if servidor is None:
        session.close()
        raise HTTPException(status_code=404, detail="Servidor não encontrado")

    session.delete(servidor)
    session.commit()
    session.close()
    return {"mensagem": "Servidor excluído com sucesso"}

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

@app.post("/membro")
def criar_membro(dados: MembroEntrada):

    session = SessionLocal()
    session.add(Membro(**dados.model_dump(by_alias=False)))
    session.commit()
    session.close()
    return {"mensagem": "Membro criado com sucesso"}

@app.put("/membro/{cracha}")
def alterar_membro(cracha: int, dados: MembroEntrada):

    session = SessionLocal()
    membro = session.query(Membro).filter(Membro.cracha == cracha).first()
    if membro is None:
        session.close()
        raise HTTPException(status_code=404, detail="Membro não encontrado")

    for campo, valor in dados.model_dump(by_alias=False).items():
        setattr(membro, campo, valor)

    session.commit()
    session.close()
    return {"mensagem": "Membro alterado com sucesso"}

@app.delete("/membro/{cracha}")
def excluir_membro(cracha: int):

    session = SessionLocal()
    membro = session.query(Membro).filter(Membro.cracha == cracha).first()
    if membro is None:
        session.close()
        raise HTTPException(status_code=404, detail="Membro não encontrado")

    session.delete(membro)
    session.commit()
    session.close()
    return {"mensagem": "Membro excluído com sucesso"}

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

@app.post("/cargo")
def criar_cargo(dados: CargoEntrada):

    session = SessionLocal()
    session.add(Cargo(**dados.model_dump(by_alias=False)))
    session.commit()
    session.close()
    return {"mensagem": "Cargo criado com sucesso"}

@app.put("/cargo/{patente}")
def alterar_cargo(patente: int, dados: CargoEntrada):

    session = SessionLocal()
    cargo = session.query(Cargo).filter(Cargo.patente == patente).first()
    if cargo is None:
        session.close()
        raise HTTPException(status_code=404, detail="Cargo não encontrado")

    for campo, valor in dados.model_dump(by_alias=False).items():
        setattr(cargo, campo, valor)

    session.commit()
    session.close()
    return {"mensagem": "Cargo alterado com sucesso"}

@app.delete("/cargo/{patente}")
def excluir_cargo(patente: int):

    session = SessionLocal()
    cargo = session.query(Cargo).filter(Cargo.patente == patente).first()
    if cargo is None:
        session.close()
        raise HTTPException(status_code=404, detail="Cargo não encontrado")

    session.delete(cargo)
    session.commit()
    session.close()
    return {"mensagem": "Cargo excluído com sucesso"}

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

@app.post("/categoria_canal")
def criar_categoria(dados: CategoriaEntrada):

    session = SessionLocal()
    session.add(Categoria(**dados.model_dump(by_alias=False)))
    session.commit()
    session.close()
    return {"mensagem": "Categoria criada com sucesso"}

@app.put("/categoria_canal/{secao}")
def alterar_categoria(secao: int, dados: CategoriaEntrada):

    session = SessionLocal()
    categoria = session.query(Categoria).filter(Categoria.secao == secao).first()
    if categoria is None:
        session.close()
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    for campo, valor in dados.model_dump(by_alias=False).items():
        setattr(categoria, campo, valor)

    session.commit()
    session.close()
    return {"mensagem": "Categoria alterada com sucesso"}

@app.delete("/categoria_canal/{secao}")
def excluir_categoria(secao: int):

    session = SessionLocal()
    categoria = session.query(Categoria).filter(Categoria.secao == secao).first()
    if categoria is None:
        session.close()
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    session.delete(categoria)
    session.commit()
    session.close()
    return {"mensagem": "Categoria excluída com sucesso"}

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

@app.post("/canal")
def criar_canal(dados: CanalEntrada):

    session = SessionLocal()
    session.add(Canal(**dados.model_dump(by_alias=False)))
    session.commit()
    session.close()
    return {"mensagem": "Canal criado com sucesso"}

@app.put("/canal/{sala}")
def alterar_canal(sala: int, dados: CanalEntrada):

    session = SessionLocal()
    canal = session.query(Canal).filter(Canal.sala == sala).first()
    if canal is None:
        session.close()
        raise HTTPException(status_code=404, detail="Canal não encontrado")

    for campo, valor in dados.model_dump(by_alias=False).items():
        setattr(canal, campo, valor)

    session.commit()
    session.close()
    return {"mensagem": "Canal alterado com sucesso"}

@app.delete("/canal/{sala}")
def excluir_canal(sala: int):

    session = SessionLocal()
    canal = session.query(Canal).filter(Canal.sala == sala).first()
    if canal is None:
        session.close()
        raise HTTPException(status_code=404, detail="Canal não encontrado")

    session.delete(canal)
    session.commit()
    session.close()
    return {"mensagem": "Canal excluído com sucesso"}

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

@app.post("/convite")
def criar_convite(dados: ConviteEntrada):

    session = SessionLocal()
    session.add(Convite(**dados.model_dump(by_alias=False)))
    session.commit()
    session.close()
    return {"mensagem": "Convite criado com sucesso"}

@app.put("/convite/{passe}")
def alterar_convite(passe: int, dados: ConviteEntrada):

    session = SessionLocal()
    convite = session.query(Convite).filter(Convite.passe == passe).first()
    if convite is None:
        session.close()
        raise HTTPException(status_code=404, detail="Convite não encontrado")

    for campo, valor in dados.model_dump(by_alias=False).items():
        setattr(convite, campo, valor)

    session.commit()
    session.close()
    return {"mensagem": "Convite alterado com sucesso"}

@app.delete("/convite/{passe}")
def excluir_convite(passe: int):

    session = SessionLocal()
    convite = session.query(Convite).filter(Convite.passe == passe).first()
    if convite is None:
        session.close()
        raise HTTPException(status_code=404, detail="Convite não encontrado")

    session.delete(convite)
    session.commit()
    session.close()
    return {"mensagem": "Convite excluído com sucesso"}

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

@app.post("/banimento")
def criar_banimento(dados: BanimentoEntrada):

    session = SessionLocal()
    session.add(Banimento(**dados.model_dump(by_alias=False)))
    session.commit()
    session.close()
    return {"mensagem": "Banimento criado com sucesso"}

@app.put("/banimento/{veto}")
def alterar_banimento(veto: int, dados: BanimentoEntrada):

    session = SessionLocal()
    banimento = session.query(Banimento).filter(Banimento.veto == veto).first()
    if banimento is None:
        session.close()
        raise HTTPException(status_code=404, detail="Banimento não encontrado")

    for campo, valor in dados.model_dump(by_alias=False).items():
        setattr(banimento, campo, valor)

    session.commit()
    session.close()
    return {"mensagem": "Banimento alterado com sucesso"}

@app.delete("/banimento/{veto}")
def excluir_banimento(veto: int):

    session = SessionLocal()
    banimento = session.query(Banimento).filter(Banimento.veto == veto).first()
    if banimento is None:
        session.close()
        raise HTTPException(status_code=404, detail="Banimento não encontrado")

    session.delete(banimento)
    session.commit()
    session.close()
    return {"mensagem": "Banimento excluído com sucesso"}
