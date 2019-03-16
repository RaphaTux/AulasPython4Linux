# ler tres numeros e encontrar o maior 

num1 = int(input( 'Digite um numero ' ))
num2 = int(input( 'Digite um numero ' ))
num3 = int(input( 'Digite um numero ' ))

if num1 > num2 and num1 > num3:
    maior = num1
    ordem = 'primeiro '
elif num2 > num1 and num2 > num3:
    maior = num2
    ordem = 'segundo '
else:
    maior = num3
    ordem = 'terceiro '

print( 'O numero maior é %d '%maior + 'que foi o ' + ordem + 'numero digitado' )




