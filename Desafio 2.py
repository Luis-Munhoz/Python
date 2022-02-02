# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:35:07 2021

@author: Luís Fernando
"""
import numpy as np
class aviao: #crio a classe
     def __init__(self, S, b, CLmax, C_D0, h): #Construtor da classe
         self.S = S
         self.b = b #Atributos da classe
         self.CLmax = CLmax
         self. C_D0 = C_D0
         self.h = h
         self.AR = (self.b**2)/self.S
         self.K = 1/(3.14*0.75*self.AR)

 #Método da classe
     def v_Stol(self, W, rho): # Argumentos do método (W e rho) #crio funções dentro da classe
         V_stol = (2*W/(rho*self.S*self.CLmax))**0.5
         return V_stol

     def efeito_Solo(self):
         zw = 16 * self.h /self.b
         phi = (zw ** 2) / (1 + zw ** 2)
         return phi

     def sustentação(self, V, CL, rho):
         L = 0.5 * (V ** 2) * rho * self.S * CL
         return L

     def arrasto(self, V, CL, rho):
         D = (0.5* (V ** 2)* rho* self.S* (self.C_D0 + self.efeito_Solo() * self.K * CL ** 2))
         return D

     def CLL0_Ideal(self, mi):
         cll0 = np.pi*0.717*self.AR*mi/(2*self.efeito_Solo())
         return cll0

     def distancia_decolagem(self, W, rho, mi):
         T = 33.207

         vlo = self.v_Stol(W, rho)*1.2
         CLLO = self.CLL0_Ideal(mi)

         L = self.sustentação(0.7*vlo, CLLO, rho)
         D = self.arrasto(0.7*vlo, CLLO, rho)

         slo = (1.44*(W**2))/(9.81*self.S*rho*self.CLmax*(T - (D + mi*(W - L))))
         return slo
A= aviao(0.9,2.48,1.65,0.022,0.35) #usei a classe
B= aviao(0.9,2.48,1.65,0.022,0.35).efeito_Solo() #usei uma função dentro da classe
C= aviao(0.9,2.48,1.65,0.022,0.35).arrasto(10,2.4,1)
print(B)
