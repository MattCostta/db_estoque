import mysql.connector
from class_product import Produto
from class_fabri import Fabricante


class Estoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='db_estoque'
        )
        self.meu_cursor = self.conexao.cursor()

    def salvar_fabricantes(self, cod, nome):
        obj_fabricante = Fabricante(cod, nome)
        comando_sql = f'insert into Fabricantes (nome) value ("{obj_fabricante.nome}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def salvar_produtos(self, cod, nome, fabricante, quantidade):
        obj_produto = Produto(cod, nome, fabricante, quantidade)
        comando_sql = f'insert into Produtos (nome, fabricante, quantidade) value ("{obj_produto.nome}", (select nome from Fabricantes where id = {obj_produto.fabricante}), {obj_produto.quantidade});'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def listar(self, tabela):
        comando_sql = f'select * from {tabela}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def listar_tabelas(self):
        comando_sql = f'show tables;'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_tabela(self, tabela, atributo, valor, cod):
        comando_sql = f'update {tabela} set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def excluir(self, tabela, cod):
        comando_sql = f'delete from {tabela} where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()