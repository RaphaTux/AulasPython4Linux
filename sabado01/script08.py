#conte quantas consoantes ha no texto 


frase = "Wake up Grab a brush and put a little (makeup) Grab a brush and put a little Hide the scars to fade away the (shakeup) Hide the scars to fade away the Why'd you leave the keys upon the table? Here you go create another fable You wanted to Grab a brush and put a little makeup You wanted to Hide the scars to fade away the shakeup You wanted to Why'd you leave the keys upon the table? You wanted to"

frase = frase.strip()
frase = frase.upper()
qtdCons = 0

rejeita = 'aeiouAEIOU ?()\t'
for caracter in frase:
    if caracter not in rejeita: 
        qtdCons = qtdCons + 1

print(qtdCons)


rejeita = 'aeiouAEIOU ?()\t'
c = 0 
for i in frase:
    if i not in rejeita:
        c += 1
print('total : %d' %c)

