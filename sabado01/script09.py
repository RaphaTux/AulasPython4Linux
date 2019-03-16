#leia a data de nascimento do usuario e imprima a data com 
#o mesm por extenso 

extenso = ''
dataNasc = input("Digite a sua data de nascimento ")
dataNasc = dataNasc.split('/')

dia = dataNasc[0]
mes = dataNasc[1]
ano = dataNasc[2]

if mes == '01':
   mesExtenso = ' Janeiro'
elif mes == '02':
       mesExtenso = 'Fevereiro'
elif mes == '03':
       mesExtenso = 'marco'
elif mes == '04':
       mesExtenso = 'Abril'
elif mes == '05':
       mesExtenso = 'Maio'
elif mes == '06':
       mesExtenso = 'Junho'
elif mes == '07':
      mesExtenso = 'Julho'
elif mes == '08':
       mesExtenso = 'Agosto'
elif mes == '09':
       mesExtenso = 'Setembro'
elif mes == '10':
       mesExtenso = 'Outubro'
elif mes == '11':
       mesExtenso = 'Novembro'
else:
    mesExtenso = 'Dezembro'
print('voce nasceu dia '+ dia + ' de ' + mesExtenso + ' de '+ ano )


dia,mes,ano = input('data:').split('/')
meses =  [ 'Janeiro','Fevereiro','Marco','Abril','maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro' ]  

print( 'nasceu em {} de {} de {} '.format(dia,meses[int(mes)-1,ano]))




