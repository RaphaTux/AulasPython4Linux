





exit()
#uma empresa de telefoni cobra r$ 0.20 por minimo abaixo de 
#200 min , entre 200 e 400 minutos o preco é r$ 0.18 
#acima de 400 o preco é r$ 0.15
#calcule a conta de telefone tendo como entrada os minutos 

minUtilizados = float(input( 'digite a quantidade de minutos utilizados '))

if minUtilizados < 200 : 
    totalConta = minUtilizados * 0.20
elif  minUtilizados <= 400 : 
    totalConta = minUtilizados * 0.18
else:
    totalConta = minUtilizados * 0.15
       
print( 'A valor da sua conta é R$ %.2f ',%totalConta )


exit()
#if else 
idade = int(input( 'Digite a sua idade? '))
habilitacao = input('possui habilitação? ' ) 

if habilitacao.lower().strip() == 'sim' and idade >= 18:
    print ( 'voce pode dirigir' )
else:
    print( 'voce não pode dirigir' )



exit()
velocidade  = float(input( 'Digite velocidade ' )) 

if velocidade > 100 :
    print('Voce foi multado')
else:
    print( 'ta suave ' )
