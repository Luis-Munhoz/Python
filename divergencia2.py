import numpy as np

#ABAIXO O CODIGO FEITO COM CLASSES E FUNÇÕES

#Como funciona uma classe?

#R: No python, a classe é um ambiente novo dentro do seu codigo, dentro dela voce pode criar codigos separadamente.
# Uma das vantagens fica na parte de organização e otimização, pois voce consegue desmembrar um codigo extenso em outros pequenos codigos
# Em outras palavras, A classe seria como um ambiente global

# Para criar uma nova classe no python, basta utilizar o comando class nome_qualquer(atributos).

# O que é função?

#R: A função tem quase a mesma definição de classe, porém a função tem por finalidade otimizar um processo repetido, utilizando
# armazenagem de variaveis, ou seja, voce atribui as variaveis necessarias e ele ja te fornece o resultado sem voce precisar reescrever o codigo
# A função tem como maior vantagem a otimização de processos repetitivos.
# Em outras palavras, a função seria como um ambiente local

# Para criar uma nova classe no python, basta utilizar o comando class nome_qualquer(atributos).
# Ao finalizar uma função e desejar retornar apenas um valor basta utilizar o return "valor desejado"

# Classes e Funções:

# Geralmente nas programações intermediarias, é bastante comum aliar classes e funções pelos seguintes motivos:
# Voce consegue criar um novo ambiente para seus codigos (classe) e dentro dele inserir metodos que se alteram ao voce inserir um novo valor (funções)
# Possibilidade de criar infinitas funções dentro de uma classe e interligá-las com a função "self".
#OBS: self é ultilizado quando voce tem mais de uma função com variaveis iguais e deseja interligar os seus valores
        # Para interligar as funções ultizando self, basta inserir self dentro da função da seguinte maneira função(self)
        # Para interligar as variaveis em funções diferentes basta usar o self.variavel

# Para criar uma classes com funções é necessario criar uma função ponto de partida chamada __init__(vl1,vl2.etc..)
# A função init tem como objetivo ser o ponto de inicio de conexão para todas as outras funções e classes

# Abaixo segue um exemplo do tema abordado

class div(): #criei a classe
    def __init__(self,c = 0.463, e = 0.0225,a = 340.29,v=22,K_alpha=100,rho=1.1125):  # função ponto de partida
        self.c=c
        self.e=e
        self.a=a
        self.v=v
        self.K_alpha=K_alpha
        self.alpha = np.deg2rad(np.linspace(-12,9,80))
        self.rho=rho

    def q(self):  #pressão dinamica   #exemplo de função
        self.rho1 = np.linspace(0,self.rho,80)  
        return (self.rho1*self.v**2)/2 
    def v_divergencia(self): # velocidade de divergencia para grafico
        return np.sqrt((2*self.K_alpha)/(self.e*self.c**2*self.a*self.rho1)) #comando sqrt é a função de realizar raiz quadrada
    def v_divergencia_max(self): # velocidade de divergencia para angulos negativos e positivos
        a=[]
        b=[]
        for i in range(0,80):
            if self.theta()[i] == max(self.theta()):
                a.append(self.v_divergencia()[i])
            if self.theta()[i] == min(self.theta()):
                b.append(self.v_divergencia()[i])
        p1=print("Velocidade de Divergencia para theta>0: ",a)
        p2=print("Velocidade de Divergencia para theta<0: ",b)
        return p1,p2 #retornando valor

    
    def theta(self): #angulo de ataque devido a torção
        angulo=((self.q()*self.e*self.c**2*self.a*self.alpha)/(self.K_alpha - self.q()*self.e*self.c**2*self.a))
        return angulo
    def ang_ataque_efetivo(self):
        return self.alpha + self.q()

#Chamando a classe para o usuario visualizar:
aviao = div()
# Chamando funções da classe:
velocidade= aviao.v_divergencia_max()
thetaa=aviao.theta()
vel=aviao.v_divergencia()

print("=========================================================================")

# Quando desejo alterar valores:
aviao2 = div(K_alpha=300, rho=0.5)
velocidade2=aviao2.v_divergencia_max()

#GRAFICO:

import matplotlib.pyplot as plt

fig = plt.figure()
eq= plt.axes()
eq.set(title="Análise Divergencia",xlabel="Velocidade de Divergencia(rho,K_alpha)",ylabel="theta(q,K_alpha)")
eq.plot(vel,thetaa,color='black')
plt.legend()
plt.grid()
plt.show()



