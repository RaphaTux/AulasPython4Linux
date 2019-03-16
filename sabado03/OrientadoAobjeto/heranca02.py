#!/usr/bin/python3.5

class Car():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        # definindo valor default
        self.hodometro = 0
        self.gasolina = 0

    def descricao(self):
        desc = '{} {} {}'.format(self.marca, self.modelo, self.ano)
        return desc.title()

    def ler_hodometro(self):
        print('Este carro rodou {} Km.'.format(self.hodometro))

    def atualiza_hodometro(self,kmtragem):
        if kmtragem >= self.hodometro:
            self.hodometro = kmtragem
        else:
            print('Nao da pra diminuir a kmtragem!')

    def incrementa_hodometro(self,kmtragem):
        if kmtragem >= 0:
            self.hodometro += kmtragem
        else:
            print('Nao da pra diminuir a kmtragem!')

    def enche_tanque_gas(self):
        self.gasolina = 100
        print('Gasolina {}'.format(self.gasolina))

class Bateria():
    def __init__(self,bateria = 100):
        self.bateria = bateria

    def descreve_bateria(self):
        print('Este carro tem {} KW/h de bateria.'.format(self.bateria))

    def distancia_percorre(self):
        distancia = self.bateria * 2
        print('Este carro percorre {} km com a bateria cheia'.format(distancia))

class Electric_Car(Car):
    def __init__(self,marca,modelo,ano): # cria instancia Car
        super().__init__(marca,modelo,ano)
        self.bateria = Bateria()

    def enche_tanque_gas(self):
        print('Esse carro é eletrico!')



tesla = Electric_Car('tesla', 'model s', 2016)
print(tesla.descricao())
tesla.bateria.descreve_bateria()
tesla.bateria.distancia_percorre()