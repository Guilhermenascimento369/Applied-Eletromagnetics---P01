
import numpy as np
import matplotlib.pyplot as plt

ex = int(input("Digite a amplitude em X: "))
afx= int(input("Digite o ângulo de fase em X"))
fx= afx * np.pi/180 #calculo da fase y a partir do angulo fornecido


ey = int(input("Digite a amplitude em Y: "))
afy= int(input("Digite o ângulo de fase em Y"))
fy= afy * np.pi/180 #calculo da fase y a partir do angulo fornecido

#cálculos
wt_grau= np.linspace(0,360,100) #intervalo de  a 360 para a frequencia em graus 
wt_rad= wtd* np.pi/180 #conversão para radianos
x= ex*np.cos(wt_rad+fx)
y= ey*np.cos(wt_rad+fy)


#grafico
plt.plot(x,y)
plt.grid()
plt.show()