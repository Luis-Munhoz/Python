# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:27:09 2021

@author: Luís Fernando
"""
    #importando
import ZebraLib as zb
import numpy as np 
import matplotlib.pyplot as plt
from pylab import *
def Torsão (self,Torsion,T,vh,vd,rho,y,cl,chord,cd,cm):

    
    T = (rho * cm * vd**2 * chord**2)/2 #calculo da torção para cada ponto da asa
    
    
    #Função para fazer integral
    def integral(x,y,a,b): #definindo, x varia de a até b, y é a função
        yb=[]
        xb=[]
        for i in range(0,len(y)-1):
            if x[i]>a and x[i]<b:
                xb.append(x[i])
                yb.append(y[i])
        soma=0
        for i in range(0,len(yb)-1):
            
            s1=((yb[i+1]+yb[i])/2)*(xb[i+1]-xb[i])
            s2=s1
            soma=soma+s2
        return soma
    
    
    Tdist= plt.figure(dpi = 150) #plotando grafico da distribuição de torsão pela asa
    
    ax5 = Tdist.add_axes([0,0,1,1]) 
    #ax5.plot(y,T, c = '#001F7C')
    ax5.plot(y,T, c = '#001F7C')
    ax5.set_ylabel("Distribuição de Torsão na Asa [N m / m]",fontsize=14)
    ax5.set_xlabel("Envergadura [m]",fontsize=14)
    ax5.set_facecolor('oldlace')
    ax5.grid(ls=':',lw = 0.5)
    Tdist.savefig('Tdist.jpeg',bbox_inches='tight')
    #Diagrama Momento Torsor
    
    from scipy.interpolate import InterpolatedUnivariateSpline
    
    
    d = 0.08 # [m]
    Torsion = [];
    Tb = integral(y,T,y.min(),y.max()) #calculando a área no gráfico
    
    
    f = InterpolatedUnivariateSpline(y, T, k=1)
    for Y in y: #calculando a distribuição de torsão ao longo da envergadura
        
        if Y < (-d/2) : #de uma extremidade a primeira fixação
            
            Torsion += [-f.integral(y.min(),Y) ] 
            
        elif Y > (-d/2) and Y < (d/2) : #entre fixação
            
            Torsion += [-f.integral(y.min(),Y) +Tb/2]
            
        else: #da segunda fixação até o final da asa
            
            Torsion += [-f.integral(y.min(),Y) +Tb]
            
    T = Torsion
    T_diagram = plt.figure(dpi = 150)
    
    ax6 = T_diagram.add_axes([0,0,1,1]) 
    #ax5.plot(y,T, c = '#001F7C')
    ax6.plot(y,Torsion, c = '#001F7C')
    ax6.set_ylabel("Momento Torsor [N m]",fontsize=14)
    ax6.set_xlabel("Envergadura [m]",fontsize=14)
    ax6.set_facecolor('oldlace')
    ax6.grid(ls=':',lw = 0.5)
    T_diagram.savefig('T.jpeg',bbox_inches='tight')

