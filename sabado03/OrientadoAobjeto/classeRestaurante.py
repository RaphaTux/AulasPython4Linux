#!/usr/bin/python3.5

class Restaurante():
    def __init__(self,nome,tipo,isAberto):
        self.nome = nome
        self.tipo = tipo
        self.isAberto = isAberto
    
    def descreve(self):
        print( '{} é um restaurante de comida {} \n'.format(self.nome,self.tipo))
    
    def status(self):
        if self.isAberto == True:
            print( '{} está aberto'.format(self.nome.title()))
        else:
            print( '{} está fechado'.format(self.nome.title()))

r1 = Restaurante( 'Habibs','Arabe',True)
r1.descreve()
r1.status()
r1.isAberto = False
r1.status()

r2 = Restaurante( 'Outback','Australiana',False)
r2.descreve()
r2.status()
r2.isAberto = True
r2.status()
