from database import engine

try:
    conexao = engine.connect()
    print("Banco de Dados conectado com sucesso")
    conexao.close
except Exception as erro:
    print("A conexão falhou")
    print(erro)