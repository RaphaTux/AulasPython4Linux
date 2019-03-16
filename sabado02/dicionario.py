#!/usr/bin/python3.5

print( '=============== Dicionarios  de Dicionarios   ===============' )

herois = { 'batman':{'nome':'bruce wayne','cidade':'gothan'},
           'super-man':{ 'nome':'Clark Kent','cidade':'metropolis' } }


print( 'acessando dicionario herois com a chave "nome" dentro do dicionario batman ' )
print(herois['batman']['nome'])


exit()
print( '=============== Dicionarios  de listas  ===============' )

lanche = { 'pão'    : ['integral','4 queijos' ,'italiano'],
           'queijo' :[ 'prato'   ,'cheddar'   ,'suico' ],
           'recheio':[ 'steak'   ,'frango'    ,'almondega']}

#print(lanche['pão'][2])

for k,v in lanche.items():
    print( '{} : {}\n'.format(k,v[0]))


exit()
koppa_red = {'color':'red','points':'30'}
koppa_blue = {'color':'blue','points':'50'}
koppa_green = {'color':'green','points':'10'}

koppa = [koppa_blue,koppa_green,koppa_red]
print( '=============== Lista de dicionarios  ===============' )
print(koppa)
print( '=============== Lista de dicionarios  ===============' )


koppa = []
for k in range(10):
    koppa.append(koppa_green)

for tropa in koppa[:5]:
    print(tropa)

print(len(koppa))




exit()
usuario = { 'userName':'dogjake','nome':'jake','sobrenome':'jake the dog' }

print( '=============== chave e valores ===============' )
for chave,valor in usuario.items():
    print('chave : {}'.format(chave))  
    print( 'valor : {}'.format(valor))

print( '=============== chaves  ===============' )
for chave in usuario.keys():
    print('chave : {}'.format(chave))  
    
print( '=============== valores ===============' )
for valor in usuario.values():
    print( 'valor : {}'.format(valor))

print( '=============== Ordenando o dicionario  ===============' )
for chave in sorted(usuario.keys()):
    print(chave)

exit()
# {} para dicionario 
cores = { 'red':'Vermelho', 'blue':'azul','green':'verde','gold':'dourado','silver':'prata'}
print(cores)

koppa_red = {'color':'red','points':'30'}
koppa_blue = {'color':'blue','points':'50'}
koppa_green = {'color':'green','points':'10'}

pontos = koppa_red['points']
cor = koppa_blue['color']
print( 'você ganhou {} '.format(pontos))

koppa_red[ 'eixo_x' ] = 5 
koppa_red[ 'eixo_y' ] = 15
koppa_red[ 'speed'  ] = 'rapido'
print(koppa_red)

print( 'Posiçao do koppa red {}'.format( koppa_red['eixo_x']))
if koppa_red[ 'speed' ] == 'devagar':
    andar_x = 1
elif koppa_red[ 'speed'] == 'medio':
    andar_x = 2
else:
    andar_x = 3

koppa_red[ 'eixo_x'] += andar_x
print( 'Posiçao do koppa red {}'.format( koppa_red['eixo_x']))

mago = {}
mago['cor'] = 'azul'
mago['pontos'] = '15'
print(mago)
mago['cor'] = 'verde'
print(mago['cor'])

print( '======================== deletando componente do dicionario==============' )
del mago[ 'cor']
print(mago)
