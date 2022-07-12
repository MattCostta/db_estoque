class Historico:
    def __init__(self):
        self.transacoes = []
    def compras_vendas(self):
        print('Transações: ')
        for i in self.transacoes:
            print('-', i)