#tuplas
retangulo = (100,50)
print(retangulo[0])

x = list(retangulo)
print(x)
x[0] = 80
print(x)



















exit()
viloes  = ['lex luthor','bizarro','cell','majin boo','thanos','darkseid','coringa','duas caras','pinguim','babidi']

print(viloes,len(viloes))
print(viloes[1:5])
print(viloes[:5])
print(viloes[:5:2])
print(viloes[1:-1])
print(viloes[::-1])

exit()
#ordenando lista
print("Ordenando somente para p print")
print(sorted(viloes))


print( "ordenando lista definitivamente ")
viloes.sort()
print(viloes)


print(" invertendo a lista")
viloes.reverse()

print(viloes)


