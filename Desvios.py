# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 22:01:55 2021

Desenvolvedor: Gabriel Messias
Co-desenvolvedor: Arthur Chabole
"""

import math as mat 

""" Instruções:
Para usar essa classe Erros, é preciso importa-la com:
>>> from Desvios import Erros as E

"""


class Erro:
    
    # Construção de um número com Desvio
    def __init__(self, valor, desvio):
        self.valor = valor 
        self.desvio = desvio
        
    def __str__(self):
        return f'Valor={self.valor}, erro={self.desvio}'
    
    
    # Operação de desvio para a Soma    
    def __add__(self, Erro):
        
        """Exemplo:
            from Desvios import Erro as Er
            x = Er(12, 0.05)
            y = Er(15, 0.03)
            print(x + y)
        """
        
        valor = self.valor + Erro.valor
        desvio = self.desvio + Erro.desvio
    
        return valor, desvio


    # Operação de desvio para a Subtração   
    def __sub__(self, Erro):
        """Exemplo:
            from Desvios import Erro as Er
            x = Er(12, 0.05)
            y = Er(15, 0.03)
            print(x - y)
        """
        
        valor = self.valor - Erro.valor
        desvio = self.desvio + Erro.desvio 
    
        return valor, desvio
    
    
    # Operação de desvio para a Multiplicação
    def __mul__(self, Erro):
        """Exemplo:
            from Desvios import Erro as Er
            x = Er(12, 0.05)
            y = Er(15, 0.03)
            print(x * y)
            
            or
            
            Exemplo:
            from Desvios import Erro as Er
            x = Er(12, 0.05)
            print(x * 3)
        """
        
        try:
            valor = self.valor * Erro.valor
            desvio = (self.desvio * Erro.valor) + (Erro.desvio * self.valor)
        except:
            valor = self.valor * Erro
            desvio = self.desvio * Erro
        return valor, desvio
    
    
    
    # Operação de desvio para a Divisão   
    
        """Exemplo:
            from Desvios import Erro as Er
            x = Er(12, 0.05)
            y = Er(15, 0.03)
            print(x // y)
        """
        
    def __floordiv__(self, Erro):
        valor = self.valor/ Erro.valor
        desvio = ((self.desvio * Erro.valor) + (Erro.desvio * self.valor))/Erro.valor**2
    
        return valor, desvio


    # Operação de desvio para o Cosseno EM RADIANOS
    def erro_Cos(valor, desvio):
        
        """Exemplo:
        from Desvios import Erro as Er
        vcos, dcos = Er.erro_Cos(12, 0.05)
        """
        
        valor1 = mat.cos(valor)
        desvio1 = desvio * mat.sin(valor)
    
        return print(valor1, desvio1)


    # Operação de desvio para o Seno EM RADIANOS
    def erro_Sin(valor, desvio):
        """Exemplo:
        from Desvios import Erro as Er
        vsin, dsin = Er.erro_Sin(12, 0.05)
        """
        
        valor1 = mat.sin(valor)
        desvio1 = desvio * mat.cos(valor)
    
        return print(valor1, desvio1)


    # Operação de desvio para Logaritmo
    def erro_Log(valor, desvio):
        
        """Exemplo:
        from Desvios import Erro as Er
        vlog, dlog = Er.erro_Log(12, 0.05)
        """
        valor1 = mat.log10(valor)
        desvio1 = desvio / valor
    
        return print(valor1, desvio1)
    
    
    # Operação de desvio para Exponencial
    def erro_Exp(valor, desvio, C):
        
        """Exemplo:
            from Desvios import Erro as Er
            vexp, dexp = Er.erro_Exp(12, 0.05, 4)
        """
        
        valor1 = C**valor
        desvio1 = (C**valor) * (mat.log(C)) * (desvio)
        
        #Possivel erro, C na verdade é o (e) exponencial, use mat.e no lugar de C, e retire ele
        #da entrada do método.
    
        return print(valor1, desvio1)


    # Operação de desvio para Raiz Quadrada
    def erro_Raiz(valor, desvio):
        
        """Exemplo:
            from Desvios import Erro as Er
            Vraiz, Draiz = Er.erro_Raiz(12, 0.05)
        """
        valor1 = mat.sqrt(valor)
        desvio1 = desvio / (2 * mat.sqrt(valor))
    
        return print(valor1, desvio1)
    
    
    # Operação para o Erro Percentual   
    def erro_100(Vteo: float, Vexp: float):
        
        """Exemplo:
            from Desvios import Erro as Er
            V100 = Er.erro_100(30, 29)
        """
        
        Epercent = (mat.fabs(Vteo - Vexp)) / Vteo
        
        return print (Epercent * 100 )
    
    
    
    

    
