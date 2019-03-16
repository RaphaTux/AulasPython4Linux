 
viloes = ['lex luthor','coringa','arlequina','duas caras','sinestro' , 'darkseid']

print(viloes)
vilao = 'thanos'

print( '=========Usando in list=================')

if vilao in viloes:
    print(vilao.title() + 'ta na lista')
else:
    print(vilao.title() + ' não ta na lista')
    viloes.append(vilao) 

    print(vilao.title() + ' adicionado  na lista')

    print(viloes)

print( '==========================')
#usando loop

for vilao in viloes :
    print('{} é muito mal'.format(vilao.title()) )


print( '======================For====================')

#imprimindo intervalos de numeros 
#for i in range(1,101):
#    print(i)

for i in range(90,100,2):
    print(i)


print( '==================While==========================')
soma = 0 
n = 0 

valor = list(range(-10,10))

while n < valor.__len__():
    soma = soma + valor[n]
    n += 1

print(soma)










