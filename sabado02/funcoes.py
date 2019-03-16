#! /usr/bin/python3.5
import sys

print( '==================== funções usando argv - com *args , a funçao descobre qantos argumentos foram passados  ================== ')
print(sys.argv)

for i in range(len(sys.argv)):
    print( 'parametro {}o  : {} '.format(i,sys.argv[i]))



exit()
print( '==================== funções usando *kwargs - com *args , a funçao descobre qantos argumentos foram passados  ================== ')
def descobre(**kwargs):
    print(kwargs)
    for k in kwargs.keys():
        print( 'chave: {}'.format(k))
        print( 'valor: {}'.format(kwargs[k]))

descobre(nome = 'Raphael',sobrenome='Andrade')
descobre(nome = 'servidor',ip='192.168.0.1',dominio = '4linux.com.br')

exit()
print( '==================== funções usando *args - com *args , a funçao descobre qantos argumentos foram passados  ================== ')
def calcular(*args):
    if len( args)== 1 :
        print('area: ',(args[0]*args[0]))
    elif len( args)== 2:
        print('area: ',(args[0]*args[1]))
    elif len( args)== 3:
        print('volume: ',(args[0]*args[1]*args[2]))


print( '==================== chamou a funçaão com um argumento "2"  ================== ')
calcular(2)
print( '==================== chamou a funçaão com dois  argumentos "2 , 8"  ================== ')
calcular(2,8)
print( '==================== chamou a funçaão com tres argumentos "2,5,8"  ================== ')
calcular(2,5,3)



exit()
print( '==================== funções com  mais de uma  parametro ================== ')
def animal(tipo,nome):
    print( 'eu tenho um {} e se chama {}'.format(tipo,nome))

animal('cachorro','rex')

print( '==================== funções com  mais de uma  parametro ================== ')
def animal(tipo = 'hamster',nome='hantaro'):
    print( 'eu tenho um {} e se chama {}'.format(tipo,nome))

#animal('cachorro','rex')
animal()


exit()
print( '==================== funções com  parametro ================== ')
def diga_ola(nome):
    print( 'Olá {}'.format(nome.title()))

def pergunta_nome():
    nome = input( 'Digite seu nome ' )
    diga_ola(nome)

pergunta_nome()


exit()
print( '==================== funções com  parametro ================== ')
def diga_ola(nome):
    print( 'Olá {}'.format(nome.title()))

def pergunta_nome():
    nome = input( 'Digite seu nome ' )
    return nome


n = pergunta_nome()
diga_ola(n)

exit()
print( '==================== funçõe sem parametro ================== ')
def diga_ola():
    print( 'Olá {}'.format( nome.title()))

nome = input( 'Digite seu nome ' )
diga_ola()