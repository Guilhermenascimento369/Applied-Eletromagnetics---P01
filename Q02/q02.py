import matplotlib.pyplot as plt
import numpy as np



#Cobre:
sig= float(input("Digite o fator da condutividade do material que deseja estudar: "))
sig_x= float(input("Digite a base da condutividade do material que deseja estudar: "))
sig_n= float(input("Digite o expoente da condutividade do material que deseja estudar"))

i=0
sig_xi=1
while  i < sig_n:
    i=i+1 
    sig_xi = sig_xi * sig_x 

    
ep_0=float(8.854 * (10**-12))
e_r=float(input("Digite a permissividade do material que deseja estudar: "))
n=np.linspace(2,10,100) #expoente da frequencia #100Htz a 100Ghz -> 
f=10**n #potencia de base 10 para trabalhar com Ghz
w=2*np.pi*f


tan=(sig_xi/w*e_r*ep_0)

#cond_cobre= 5.8**7
#e_cobre=1

#Vidro:
#cond_vidro= 10**-12
#er_vidro=int(10)


#Água do mar:
#cond_mar= 5
#er_mar= 81

plt.plot(tan,f)
print(tan)
plt.grid()
plt.yscale('log')
plt.xscale('log')
plt.show()