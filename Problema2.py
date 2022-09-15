import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from math import e

df = pd.read_excel("respuestas.xlsx")   
#Datos altura
aalt=df['altura'].max()
balt=df['altura'].mean()
calt=df['altura'].std()
#Datos talla
atal=df['talla'].max()
btal=df['talla'].mean()
ctal=df['talla'].std()

print('La media (mu) de la altura es: ',float(balt))
print('La desviacion estandar de la altura es: ',float(calt))
print('La media (mu) de la talla es: ',float(btal))
print('La desviacion estandar de la talla es: ',float(ctal))

#Calculo de la funcion gausiana normalizada
x1 = np.arange(50,220,1)
y1 = 1/(calt*math.sqrt(2*math.pi))*e**((-1/2)*((x1-balt)/calt)**2)

x2 = np.arange(10,50,0.1)
y2 = 1/(ctal*math.sqrt(2*math.pi))*e**((-1/2)*((x2-btal)/ctal)**2)

#calculo de la funcion gausiana no normalizada
x3 = np.arange(50,220,1)
y3 = aalt*e**((-(x3-balt)**2)/(2*calt**2))

x4 = np.arange(10,50,40/170)
y4 = atal*e**((-(x3-btal)**2)/(2*ctal**2))

#probabilidad de una persona
prob = 0
i = 0
d1=balt-calt
d2=balt+calt
inc=100/216
array=df['altura']
for i in range (216):
    if array[i] >= d1 and array[i] <= d2:
        prob = prob+inc        
print('La probabilidad e que este en la primera desviacion estandar en altura es: ', int(prob), '%')

prob = 0
i = 0
d1=btal-ctal
d2=btal+ctal
array=df['talla']
for i in range (216):
    if array[i] >= d1 and array[i] <= d2:
        prob = prob+inc        
print('La probabilidad e que este en la primera desviacion estandar en talla es: ', int(prob), '%')

#impresion de graficas

ax = plt.subplot(2,2,1)
plt.hist(df['altura'], 15, color="yellow", ec="black", density=True)
plt.plot(x1,y1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Distribucion altura normalizada')

ax = plt.subplot(2,2,2)
plt.hist(df['altura'], 15, color="yellow", ec="black")
plt.plot(x3,y3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Distribucion altura no normalizada')

###################################################################

ax = plt.subplot(2,2,3)
plt.hist(df['talla'], 15, color="blue", ec="black", density=True)
plt.plot(x2,y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Distribucion Talla normalizada')


ax = plt.subplot(2,2,4)
plt.hist(df['talla'], 15, color="blue", ec="black")
plt.plot(x4,y4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Distribucion Talla no normalizada')
plt.show()