from classe_cliente import Cliente
from classe_conta import Conta

cliente1 = Cliente('Mateus Costa','12345678-0','14/07/1997')
print(cliente1)
cliente1.imprime_dados()
conta1 = Conta(cliente1, '123-4')
conta1.deposito(float(input('Digite um valor: ')))
conta1.extrato()
cliente2 = Cliente (input('Insira seu nome: '),input('Insira seu cpf: '),input('Insira sua data de nascimento:'))
print(cliente2)
conta2= Conta(cliente2, input('Insira o numero da sua conta: '))
conta2.deposito(float(input('Digite um valor:  ')))
conta2.extrato()