import random

import matplotlib.pyplot as plt
import math

## Задание 1
P = []

def raspFunc(q, M, x):
    p = ((math.e**(-1*((x-M)**2))/(2*(q**2)))/(q*(math.sqrt(2*math.pi))))
    return p


def aprox():
    mi = math.trunc(100*random.random())+1
    print(mi)
    y = mi + (0.2)*random.random()
    return y

P = []
for i in range(10**3):
    P.append(raspFunc(1,10,aprox()))

plt.title("M=10,o=1")
plt.axis([0,20,min(P),max(P)])
plt.plot(P)
plt.show()

P = []
for i in range(10**3):
    P.append(raspFunc(0.5,10,aprox()))

plt.title("M=10,o=0.5")
plt.axis([0,20,min(P),max(P)])
plt.plot(P)
plt.show()

P = []
for i in range(10**3):
    P.append(raspFunc(1,12,aprox()))

plt.title("M=12,o=1")
plt.axis([0,20,min(P),max(P)])
plt.plot(P)
plt.show()

for i in range (3,7):
    P = []
    for j in range(10**i):
        P.append(raspFunc(2, 10, aprox()))
    t = "10**" + str(i)
    plt.title(t)
    plt.axis([0, 20, min(P), max(P)])
    plt.plot(P)
    plt.show()