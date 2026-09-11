import sqlite3
import unittest

def connect_banco(nome_banco = "escola.db"):
    conn = sqlite3.connect(nome_banco)
    return conn    

def conectar():
    conn = sqlite3.connect("escola.db")
    return conn

def criar_tabela(nome_banco = "escola.db"):

    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota REAL)
    """)

    conn.commit()
    conn.close()

def cadastro_aluno(nome: str, idade, nota,
                    nome_banco = "escola.db"):

    if nome.strip() == "":
        return "Nome do aluno não pode ficar em branco."
    
    elif idade > 22:
        return "Idade acima de 22 anos."
    
    else:
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)", (nome, idade, nota))  

        conn.commit()
        conn.close()

        return "Aluno cadastrado com sucesso!"

def delete_aluno(id, banco_teste = "banco_teste.db"):
    if id != None:
        conn = sqlite3.connect(banco_teste) #para nao apagar tudo e fazer besteira tem que colocar o "nome_banco"
        cursor = conn.cursor()

        cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))  

        conn.commit()
        conn.close()

        return True #f"O aluno de ID {id} foi deletado" foi substituido por true
    else:
        return False #"ID inserido e invalido" foi substituido por False

def update_idade_aluno(id, idade):
 

    # Quebra de regra de negócio
    if idade > 22:
        return "Idade acima de 22 anos não é permitida"

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE alunos SET idade = ? WHERE id = ?", (idade, id))
    rows_affected = cursor.rowcount

    # Caso de sucesso
    if rows_affected > 0:
        conn.commit()
        conn.close()

        return rows_affected
    
    # Aluno inexistente
    else:
        return f"Aluno com ID = {id}, não encontrado"
# quebra a regua de negócio 

