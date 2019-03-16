#!/usr/bin/python3.5
#criar classe de usuario que possui atributos 
#nome e sombrenome , um metos para descrever a classe 
#classe e um metodo para saudação 
#crie duas instancias e chame os metodos 

class Usuario():
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def descClasse(self):
        print(self.nome)
        print(self.sobrenome)
    
    def saudacao(self):
        print( 'ola! {} {} seja  bem vindo ! '.format(self.nome,self.sobrenome))
    
    #saudacao = lambda : print(self.nome)
        
nomeSobrenome = input( 'Digite seu nome e sobrenome ').split()
sNome = nomeSobrenome[0]
sSobrenome = nomeSobrenome[1]
user1 = Usuario( sNome,sSobrenome)
user1.descClasse()
user1.saudacao()

nomeSobrenome = input( 'Digite seu nome e sobrenome ').split()
sNome = nomeSobrenome[0]
sSobrenome = nomeSobrenome[1]
user2 = Usuario( sNome,sSobrenome)
user2.descClasse()
user2.saudacao()

