#!/usr/bin/python3.5

class Dog():
    """escrever para oque serve sua classe """
    dono = None
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print( '{} está sentado agora '.format(self.nome.title()))

    def deitar(self):
        print( '{} está deitado agora  '.format(self.nome.title()))
    
    def latir(self):
        print( 'Au ! au ! au !' )
        
meu_dog = Dog( 'Rex',2)
seu_dog = Dog( 'jake',5 )
print( 'meu dog tem {} anos e se chama {}'.format(meu_dog.idade,meu_dog.nome))
print( 'seu dog tem {} anos e se chama {}'.format(seu_dog.idade,seu_dog.nome))
meu_dog.dono = input('digite o novo nome do dono ')
print('o dono do {} é o {} '.format(meu_dog.nome,meu_dog.dono) )
meu_dog.sentar()
seu_dog.deitar()

meu_dog.latir()



