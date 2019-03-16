#!/usr/bin/python3.5

#Criar classe carro com atributos marca , modelo, ano , e hodometro sendo hodometro = 0 
#faça um metodo para descrever a classe e outro para ler o odometro 

class Carro():
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.hodometro = 0
        self.gasolina = 0 

    def descrever(self):
        if self.hodometro > 0:
            print( 'marca :{} , modelo: {} , ano:{} ,hodometro : {}'.format(self.marca,self.modelo,self.ano,self.hodometro))
        else:
            print( 'marca :{} , modelo: {} , ano:{}'.format(self.marca,self.modelo,self.ano))

    def lerHodometro(self):
        print( 'hodometro : {}'.format(self.hodometro))
    
    def atualiza_hodometro(self,kmtragem):
        if kmtragem >= self.hodometro:
            self.hodometro = kmtragem
        else:
            print( ' não é permitido diminuir a kilometragem' )
    
    def incrementa_hodometro(self,km):
        if km >= 0:
            self.hodometro += km
        else:
            print( ' não é permitido diminuir a kilometragem' )
    
    def enche_tanque(self):
        self.gasolina = 100
        print( 'Gasolina {}'.format(self.gasolina))

class Eletric_Car(Carro):
    def __init__(self,marca,modelo,ano):
        super().__init__(marca,modelo,ano)
        self.bateria = 70
    
    def descrever(self):
        print( 'marca :{} , modelo: {} , ano:{} ,hodometro : {}'.format(self.marca,self.modelo,self.ano,self.hodometro))
        print( ' Carro tem {} Kmh de bateria'.format( self.bateria))
    
    def enche_tanque(self):
        print( 'Este carro é eletrico ' )

#marcaCarro = input( 'Digite a marca do carro ' ).title()
#modeloCarro = input( 'Digite a modelo do carro ' ).title()
#anoCarro = input( 'Digite o ano do carro ' )

marcaCarro = 'honda'
modeloCarro = 'Fit'
anoCarro = 2010

carro = Carro( marcaCarro,modeloCarro,anoCarro)
carro.descrever()
carro.lerHodometro()

hodometroCarro = int(input( 'Digite a quantidade de kilometros  do carro ' ))
carro.atualiza_hodometro(hodometroCarro)  
carro.lerHodometro()
carro.descrever()

carro.incrementa_hodometro(500)
carro.incrementa_hodometro(500)
carro.lerHodometro()
carro.enche_tanque()

print( " ----------------- carro eletrico -------------")
marcaCarro = 'Tesla'
modeloCarro = 'model s '
anoCarro = 2020

carroEletrico = Eletric_Car(marcaCarro,modeloCarro,anoCarro)
carroEletrico.descrever()

hodometroCarro = int(input( 'Digite a quantidade de kilometros  do carro ' ))
carroEletrico.atualiza_hodometro(hodometroCarro)  
carroEletrico.lerHodometro()
carroEletrico.descrever()
carroEletrico.enche_tanque()

carroEletrico.incrementa_hodometro(500)
carroEletrico.incrementa_hodometro(500)
carroEletrico.lerHodometro()