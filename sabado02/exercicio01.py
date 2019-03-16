#! /usr/bin/python3.5
#recebe uma entrada com uma conta ex. "2+6"
#fazer o calculo e mostrar resultado 


print ( '========================== do meu jeito  =====================' ) 
operacao = 0

def splita(frase):
    for caracter in frase:
        modificado = caracter+' '
    return modificado


def calculadora(*args):
    operacao = input( "Digite oque voce deseja calcular ")
    operacao = splita(operacao)
    #operacao = operacao.split()

    if operacao[1] == '+':
        resultado = int(operacao[0]) + int(operacao[2]) 
    elif operacao[1] == '-':
        resultado = int(operacao[0]) + int(operacao[2])
    elif operacao[1] == '*':
        resultado = int(operacao[0]) * int(operacao[2])
    elif operacao[1] == '/':
        resultado = float(operacao[0]) / float(operacao[2])
    else:
        print( "Digite um operador valido")
        exit()

    dicionario = {  }
    print( 'O resultado da operacao é {}'.format(resultado))

calculadora(operacao)
print ( '===============================================' )