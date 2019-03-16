#!/usr/bin/python3.5

with open( 'arquivo1.txt','a'  ) as arquivo:
    arquivo.write( 'escrevendo no arquivo outra vez  \n!' )


exit()
# w apaga o arquivo e escreve 
# a appenda 
with open( 'arquivo1.txt','w'  ) as arquivo:
    arquivo.write( 'escrevendo no arquivo!' )


exit()
with open( 'arquivo1.txt' ) as arquivo:
    linhas = arquivo.readlines

string = ''

for linha in linhas:
    string += linha.rstrip()


exit()

print( "========================quebra linhas e cria uma lista ========================")
with open( 'arquivo1.txt' ) as arquivo:
    linhas = arquivo.readlines()
print(linhas)

exit()
with open( 'arquivo1.txt' ) as arquivo:
    for linha in arquivo:
        print(linha)


exit()
arquivo = open( 'arquivo1.txt')
print(arquivo.read())
arquivo.close()