class Cliente:
    def __init__(self,nome,cpf,dataNasc):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc

    def imprime_dados(self):
        print(f'nome: {self.nome}\n' f'CPF: {self.cpf}'f'\n DataNasc: {self.dataNasc}')