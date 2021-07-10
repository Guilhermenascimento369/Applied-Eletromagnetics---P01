import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits import matplot3d

ax = plt.axes(projection = "3d")

E_0= float(input("Forneça o valor de E0"))
z= int(input("Digite o valor de Z"))
n= int(input("Digite o expoente da frequência"))
imp= float(376.73) #inpedância característica no espaço livre


#def e_function(t,b):
    #return np.cos(2* np.pi * (10**6)*t - b)

t=np.linspace (0,5,100)
f=10**n
w=2*np.pi*f

ep_0=float(8.854 * (10**-12))
mi_0=float(1.256*(10**-6))

bth= w*np.sqrt(mi_0*ep_0)

e=E_0*np.cos(w*t-bth*z)
h=((E_0/imp)*np.cos(w*t-bth*z))

#T,B = np.meshgrid(t,b)
#Z= e_function(T,B)

#ax.plot_surface(T,B,Z)

plt.plot(e,t,zdir='y')
plt.plot(h,t,zdir='x')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()