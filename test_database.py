import unittest
import sqlite3
import os
import database2 as db        


class TestDeleteAluno(unittest.TestCase): # cria a classe de test_deletar_aluno_com_sucesso

    def setUp(self):
    #cria caixa de areia(banco de dados)

        self.banco_teste = "banco_teste.db"
        db.criar_tabela(nome_banco=self.banco_teste)
        
    def tearDown(self):
        if os.path.exists(self.banco_teste):
            os.remove(self.banco_teste)
    
    def test_delete_aluno_com_sucesso(self):

        db.cadastro_aluno("Lohan Victor", 17, 1 ,self.banco_teste)
            
        conn = sqlite3.connect(self.banco_teste)# gera conexão
        cursor = conn.cursor() # gera um cursorr
        cursor.execute ("SELECT id FROM alunos WHERE nome = 'Lohan Victor'") 
        id = cursor.fetchone()[0]

        print(f"O id do banco {id}")
        conn.close()

        msg = db.delete_aluno(id, self.banco_teste)

        self.assertTrue(msg) # assert é o teste final 

#precisa saber fazer o crud e front e um teste de sucesso amanha
