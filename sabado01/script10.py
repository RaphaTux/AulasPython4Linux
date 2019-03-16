pot = []
for valor in range(1,11):
    if valor % 2 == 0:
        pot.append(valor**2)

print("================ Com for =========" )
print(pot)

#list compreention 
pot = [(valor**2)for valor in range(1,11) if valor % 2 == 0]
print("================ somente os pares ==========")
print(pot)

print('================ somente os impares =======')
pot = [(valor**2)for valor in range(1,11) if valor % 2 != 0]
print(pot)

