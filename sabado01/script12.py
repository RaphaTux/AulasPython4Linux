#leia uma palavra e troque as vovgais pos asterisco

palavra = input("Digite uma palavra ")
palavraTrocada = ''

vogais = 'aeiouAEIOU'
for caracter in palavra: 
    if caracter in vogais:
        caracter = '*'
        palavraTrocada = palavraTrocada + caracter
    else:
        palavraTrocada = palavraTrocada + caracter

print(palavraTrocada)



