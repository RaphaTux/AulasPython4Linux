#!/usr/bin/python3

# Dado o cenario abaixo abstraia uma conta bancaria utilizando 
# programacao orientada a objeto, crie metodos para transferencia,
# saque e deposito e utilize heranca se necessario tambem

# Joao possuia 30k em sua CC e uma poupança com saldo zerado, 
# entao ele transferiu 3k para CC de Maria que ja possuia 2k 
# em sua CC e depois disso Joao transferiu 5k para sua poupanca
# Após um mês a poupança de Joao rendeu 0.6% do valor de seu saldo

class Conta():
    def __init__(self,titular,numero,saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def descreve(self):
        print('titular: {}\nCC: {}\nSaldo{}'.format(self.titular,self.numero,self.saldo))

    def sacar(self,valor):
        self.saldo -= valor
        return self.saldo

    def depositar(self,valor):
        self.saldo += valor
        return self.saldo

    def transferir(self,valor,conta):
        self.sacar(valor)
        conta.depositar(valor)

class Poupanca(Conta):
    def __init__(self,titular,numero,saldo):
        super().__init__(titular,numero,saldo)
        self.juros = 1.006

    def descreve(self):
        print('titular: {}\nPoupanca: {}\nSaldo{}'.format(self.titular,self.numero,self.saldo))

    def render(self):
        self.saldo *= self.juros
        return self.saldo

joao_cc = Conta('joao',12345,30000)
joao_pp = Poupanca('joao',54321,0)
maria_cc = Conta('maria',98765,2000)

joao_cc.transferir(3000,maria_cc)
joao_cc.descreve()
maria_cc.descreve()

joao_cc.transferir(5000,joao_pp)
joao_cc.descreve()
joao_pp.descreve()

joao_pp.render()
joao_pp.descreve()