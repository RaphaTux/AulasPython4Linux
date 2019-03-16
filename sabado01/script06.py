#Crianndo listas
heroisList = ['superman','batman','mulher maravilha','flash','lanterna verde']

#print(heroisList)

#verificar tamanho da lista
#print(len(heroisList))

heroisList[2] = 5

print(heroisList)

#inserindo em uma posição  uma list
heroisList.insert(2,'Robin')
print(heroisList,len(heroisList))

#deletando posiçaõ da lista 
del heroisList[3]
print(heroisList,len(heroisList))

p = heroisList.pop()
print(heroisList,len(heroisList))

p = heroisList.pop(1)
print(heroisList,len(heroisList))

heroisList.remove('flash')
print(heroisList,len(heroisList))

#adicionando item em uma lista 
heroisList = []
heroisList.append( input('digite o super heroi'))
print(heroisList,len(heroisList))






