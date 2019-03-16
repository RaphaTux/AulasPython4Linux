#!/usr/bin/python3.5

#lambda 
calcula = {
        'soma' : lambda x,y : x+y,
        'subtrai' : lambda x,y : x-y,
        'multiplica' : lambda x,y : x*y,
        'divide' : lambda x,y : x/y
}
funcao = calcula['soma']
print(funcao(10,15))
print(calcula['soma'](10,15))






exit()
tamanho = lambda palavra : [len(p) for p in palavra]
frase = 'teste lambda string'.split()
print(frase)
print(tamanho(frase))



exit()

def tamanho(palavra):
    return [len(p) for p in palavra]

frase = 'teste lambda string'.split()
print(frase)
print(tamanho(frase))

exit()
def multiplica(n):
    return lambda a : a*n

print( 'dobro = multiplica(2)' )
print( 'dobro( lambda a : a*2)' )

dobro = multiplica(2)
triplo = multiplica(3)

print(dobro(12))
print(triplo(12))



exit()
print( 'x = lambda a,b,c : a + b + c' +  'com 3 parametros ')
x = lambda a,b,c : a + b + c
print(x(6,5,10))


exit()
print( 'x = lambda a,b : a * b' +  'com 2 parametros ' )
x = lambda a,b : a * b
print( x(4,5))

exit()
print( 'x = lambda a : a+10' +  'com 1 parametros ')
x = lambda a : a+10
print(x(5))