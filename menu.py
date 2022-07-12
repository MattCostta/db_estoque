from db_estoque import Estoque

class Menu():
    def __init__(self):
        estoque = Estoque()
        while True:
            entrada=input(('1 - Listar Todas as Tabelas\n'
                        f'2 - Listar Tabelas Por Nomes\n'
                        f'3 - Cadastrar Fabriante\n'
                        f'4 - Cadastrar Produto\n'
                        f'5 - Alterar Atributo da Tabela\n'
                        f'6 - Comprar Produto\n'
                        f'7 - Vender Produto\n'
                        f'8 - Excluir\n'
                        f'0 - Sair\n: '))
            if entrada == '1':
                estoque.listar_tabelas()
            elif entrada == '2':
                estoque.listar_tabelas()
                tabela = input('Insira o nome da Tabela : ')
                estoque.listar(tabela)
            elif entrada == '3':
                cod = None
                nome = input('Insira o nome do Fabricante : ')
                estoque.salvar_fabricantes(cod, nome)
            elif entrada == '4':
                cod = None
                nome = input('Insira o nome do produto : ')
                estoque.listar('Fabricantes')
                fabricante = input('Insira o código do fabricante : ')
                quantidade = int(input('Qual a quantidade : '))
                estoque.salvar_produtos(cod, nome, fabricante, quantidade)
            elif entrada == '5':
                tabela=input('Insira o nome da Tabela : ')
                atributo=input('Insira o nome da coluna : ')
                valor=input('Insira a mudança : ')
                cod=input('Insira o id a ser alterado : ')
                estoque.alterar_tabela(tabela, atributo, valor, cod)
            elif entrada == '8':
                estoque.listar_tabelas()
                tabela = input('Insira o nome da Tabela : ')
                estoque.listar(tabela)
                cod=input('Insira o código a ser excluído : ')
                estoque.excluir(tabela,cod)
            elif entrada == '0':
                print('Obrigado e volte sempre :D')
                break
            else:
                print('Opção Inválida!')