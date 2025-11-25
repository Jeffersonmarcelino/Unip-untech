import sqlite3

# Conectar ao banco (cria automaticamente se não existir)
con = sqlite3.connect('sistema_academico.db')
cur = con.cursor()

# Criar tabela de usuários
cur.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    perfil TEXT NOT NULL
)
''')

# Inserir usuários iniciais (somente se a tabela estiver vazia)
cur.execute("SELECT COUNT(*) FROM usuarios")
if cur.fetchone()[0] == 0:
    cur.execute("INSERT INTO usuarios (nome, usuario, senha, perfil) VALUES ('Ana Souza', 'coordenador', '123', 'Coordenador')")
    cur.execute("INSERT INTO usuarios (nome, usuario, senha, perfil) VALUES ('Carlos Lima', 'professor', '123', 'Professor')")
    cur.execute("INSERT INTO usuarios (nome, usuario, senha, perfil) VALUES ('João Pedro', 'aluno', '123', 'Aluno')")
    con.commit()

con.close()
print("Banco de dados criado e usuários inseridos com sucesso!")
