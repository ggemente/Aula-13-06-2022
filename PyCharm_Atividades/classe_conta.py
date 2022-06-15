from classe_historico import informativo
class Conta:
    def __init__(self,objeto, numero, saldo=0.0):
        self.titular = objeto.nome
        self.numero = numero
        self.saldo = saldo
        #
        self.historico = informativo()

    def extrato(self):
        print(f'Titular: {self.titular}' f'\nNumero: {self.numero}' f'\n Saldo:{self.saldo}')
        self.historico.transacoes_bancarias()

    def deposito(self, valor:float):
        self.saldo += valor
        #
        self.historico.transacoes.append(f'depósito de {valor}')
        return self.saldo

    def saque(self, valor:float):
        self.saldo -= valor


    def recebe_transferencia(self, valor, origem):
        self.saldo += valor
        self.historico.transacoes.append(f'transferencia de {valor} da conta {origem.numero}')
