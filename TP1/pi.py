import math
from decimal import Decimal

print()
print("a) π con librería math")
aPI = math.pi
print(aPI)

print()
print("b) π Gauss-Legendre con float")
def gaussLegendre(a,b,t,p,n):
    for i in range(n):
        x = (a + b)/2.0
        y = math.sqrt(a*b)
        tn = t - p *((a - x)**2.0)
        pn = 2.0*p

        pi = ((x+y)**2.0  / (4.0*tn))
        a, b, t, p = x, y, tn, pn
    return pi
    
print(gaussLegendre(1.0,1.0/math.sqrt(2.0),1.0/4.0,1.0,4))

print()
print("c) π Gauss-Legendre con Decimal")
def gaussLegendre(a,b,t,p,n):
    for i in range(n):
        x = (a + b)/2
        y = math.sqrt(a*b)
        tn = t - p *((a - x)**2)
        pn = 2*p

        pi = (Decimal(((x+y)**2  / (4*tn))))
        a, b, t, p = x, y, tn, pn
    return pi
    
print(gaussLegendre(1,1/math.sqrt(2),(1/4),1,4))

print()
print("d) π con el algoritmo de Espita (Spigot)")
def espita(n):
    pi=0
    for i in range(n):
        pi += ((math.factorial(i)**2)*(2**(i+1))/math.factorial(2*i+1))
    return pi
print (espita(100))

print()
print("Analisis de resultados")
print(" 2) Calcular area de circunferencia con cada π obtenido (tomamos r = 2)")
def areaCalculator(pi,r):
    return (pi*(r**2))

print(areaCalculator(aPI,2))
print(areaCalculator(gaussLegendre(1.0,1.0/math.sqrt(2.0),1.0/4.0,1.0,5),2))
print(areaCalculator(gaussLegendre(1,1/math.sqrt(2),(1/4),1,5),2))
print(areaCalculator(espita(100),2))