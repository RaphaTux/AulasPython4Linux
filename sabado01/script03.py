
# capturar nome informado pelo usuario em uma variavel aluno 
# calcular a media de 4 notas que vao de 1 a 10 que tambem serao dadas ppelo usuario 
#printar a media 


nomeAluno = input('Digite seu nome ' ) 
nomeAluno.upper()
nota1 = int( input('   digite a primeira nota '))
nota2 = int( input('   digite a segunda nota '))
nota3 = int( input('   digite a terceira nota '))
nota4 = int( input('   digite a ultima nota '))


media = (nota1+nota2+nota3+nota4)/4
print ('A média do aluno '+ nomeAluno + ' é '+ str(media) )
print ('o aluno ' + nomeAluno + 'tem media: %.1f\n' %media)

