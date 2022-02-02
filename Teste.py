from matplotlib import pyplot as plt
import ZebraLib as zb
class Asa:
 def __init__ (self,nome,b,S,CLmax,AR):
    self.nome = nome
    self.b = b
    self.S = S
    self.CLmax = CLmax
    self.AR = b**2/S

wing=Asa('wing',2,1.32,0.81,0)
W=80
rho=1.201
V=18
Vestol=(2*W/rho*V*2*wing.CLmax)*0.5
print('os parametros são:', wing.nome,  wing.S,  wing.b,  wing.CLmax,  wing.AR)
plt.plot([0.5,1,32], [Vestol,2000,2500])



