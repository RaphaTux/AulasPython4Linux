#!/usr/bin/python3.5
#criar classe usuario com atributo nome , sobrenome ,username ,e senha 
#criar metodos de descrever a classe
# criar metodos saudaçao 
# criametodo para realizar logiin 
# contar as tentativas de login e resetar a quantdade de tentativas de loguin qunado o usuario logar    

comCadastro = False
class Usuario():
    
        
    def __init__(self,nome,sobrenome,userName,senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.userName = userName
        self.senha = senha
        self.icont = 0
        
    def descClasse(self):
        print(self.nome)
        print(self.sobrenome)
    
    def cadastraUsuario(self):
        self.nome = input( "Digite seu nome ")
        self.sobrenome = input( "Digite seu sobrenome ")
        self.userName = input( "Digite seu usuario ")
        self.senha = input( "Digite sua senha " )
        comCadastro = True


    def saudacao(self):
        print( 'ola! {} {} seja  bem vindo ! '.format(self.nome,self.sobrenome))

    def efetuaLogin(self,userName,senha):
        if userName != self.userName or senha != self.senha:
            print( " Voce digitou usuario ou senha invalida tente novamente")
            self.icont = self.icont+1
            print( 'voce tentou {} veses '.format(self.icont))
            if self.icont == 3:
                sCadastra = input( 'voce alcançou o número máximo de tentativas desenha cadastrar este usuário ? \n digite: \n1 - Sim \n2 - Não')
                if sCadastra == '1':
                    self.cadastraUsuario()
                else:
                    exit()
        else:
            print( " Usário logado ! " )
            self.icont = 0
            print( 'numero de tentativas {} veses '.format(self.icont))
            exit()
            
if comCadastro == False:
    nome = input( "Digite seu nome ")
    sobrenome = input( "Digite seu sobrenome ")
    userName = input( "Digite seu usuario ")
    senha = input( "Digite sua senha " )
    user1 = Usuario( nome,sobrenome,userName,senha)
    user1.descClasse()
    user1.saudacao()
  
else:
    user1.descClasse()
    user1.saudacao()

while True:
    userName = input( "Digite seu usuario ")
    senha = input( "Digite sua senha " )
    user1.efetuaLogin(userName,senha)


        

