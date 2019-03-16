#!/usr/bin/python3.5

#crie um algoritmo que receba a temperatura em celcius , 
#transforme para farrenjeit e tambem de farenheit para celcius 
#faça primeiro com map 


temperatura = input( "digite a temperatura para conversão ")


def transCe(temperatura ):
    return (9/5) * temperatura + 32

def transFi(temperatura):
    return (5/9) * (temperatura - 32)

print(map(transCe,temperatura))


#temp = [transCe(temperatura)]

print (list(map(transFi,temp )))

tempCel = lambda temperatura : (9/5) * temperatura + 32
tempFar = lambda temperatura : (5/9) * (temperatura - 32)

#print(tempCel(10))

