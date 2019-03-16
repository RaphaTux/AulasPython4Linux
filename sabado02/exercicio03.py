#!/usr/bin/python3.5
#capturar  dados da esntrada com nome , estado e cpf de uma pessoa 
#adicionar os dados em um arquivo
#buscar no arquivo se pessoa existe 


def buscaTodos():
    with open( 'arquivo1.txt' ) as arquivo:
        for linha in arquivo:
            print(linha)

def adiciona( nome,estado,cpf):
    with open( 'arquivo1.txt','a'  ) as arquivo:
        arquivo.write(cpf+'-'+nome+'-'+estado+'\n')
    print( 'Adicionado !')
        
def buscar(cpf):
    with open( 'arquivo1.txt','r' ) as arquivo:
        for linha in arquivo:
            if cpf in linha:
               print( 'Foram encontrados cadastros com este Cpf \n ')
               print(linha)
            else:
              print( 'Não foram encontrados cadastros com este Cpf ') 
def sair():
    exit()

 
opcoes = { '1':adiciona , '2':buscar , '3':buscaTodos , '4':sair }    
while True:

    opcoes

    opcao = input( 'Digite a opção desejada \n 1 - adicionar \n 2 - para  buscar \n 3 - exibe todos os registros \n 4-sair'  )
    if opcao == '1':
        dados = input("Digite o nome , o estado e o cpf ").split( )
        nome,estado,cpf =  dados
        adiciona(nome,estado,cpf)
    elif opcao == '2':
        cpf = input('digite o CPF que deseja buscar ')
        buscar(cpf) 
    elif opcao == '3':
        buscaTodos()       
    elif opcao == '4':
        exit()
















#
  