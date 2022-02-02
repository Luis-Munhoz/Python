# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:03:19 2021

@author: Luís Fernando
"""
import numpy as np 
import matplotlib.pyplot as plt
from pylab import *
def dados_aerodinamica (self,vh,vd,rho,y,cl,chord,cd,cm):
    
    # Importa dados da asa recebidos da aerodinâmica
    wing_data = np.loadtxt("C:\Asa 2021.txt") #Importando dados pegar da alocação certa
    #coloca o caminho no verdinho ai em cima
    y = wing_data.T[1]                #importa envergadura                
    chord = wing_data.T[4]            #importa corda 
    cl = wing_data.T[0] #Importando coeficiente de sustentação
    cd = wing_data.T[5] #importando coeficente de arrasto
    cm = wing_data.T[6] #importando centro de massa
    rho=1.225 #densidade do ar
    vh= 17.8 #velocidade de cruzeiro
    vd = 1.25 * vh #velocidade critica de mergulho