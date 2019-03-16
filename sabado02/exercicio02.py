#!/usr/bin/python3.5
#apturar do terminal 3 agumentos  
# um que sera uma palavra , outro  comando para criptografar ou descriptografar 
#outro a chave da criptografia 
#exemplo :
#cript pedro 1 
# saida : qfesp  

import sys

def cifra(mensagem,direcao,chave):
    m = ''
    for caracter in mensagem: 
        if caracter in alfabeto:
            indice = alfabeto.index(caracter)
            m += alfabeto[(indice + direcao * chave) % len(alfabeto)]
        else:
            m += caracter
    return m    

def criptografar(mensagem,chave):
    print(cifra(mensagem,1,chave))
def descriptografar(mensagem,chave):
    print(cifra(mensagem,-1,chave))

funcao = sys.argv[1].lower()
palavra = sys.argv[2].lower()
chave = int(sys.argv[3])
alfabeto = [ 'abcdefghijklmnopkrstuvxyz']

opt={ 'cript':criptografar,'descript':descriptografar}

try:
    opt[funcao](palavra,chave)
except Exception as e :
    print( 'Erro {}'.format(e))