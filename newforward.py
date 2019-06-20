import math as m
import numpy as np

a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))
a=a*(3.1416/180.0)
b=b*(3.1416/180.0)
c=c*(3.1416/180.0)
    
x=-16.2*np.sin(b)*np.sin(c)*np.cos(a)+16.2*np.cos(a)*np.cos(b)*np.cos(c)+7.7*np.cos(a)*np.cos(b)+5.5*np.cos(a)
y=-16.2*np.sin(b)*np.sin(c)*np.sin(a)+16.2*np.sin(a)*np.cos(b)*np.cos(c)+7.7*np.sin(a)*np.cos(b)+5.5*np.sin(a)
z=16.2*np.sin(b)*np.cos(c)+7.7*np.sin(b)+16.2*np.sin(c)*np.cos(b)

x1=x*np.cos(3.1415/4)+y*np.sin(3.1415/4)
y1=x*np.sin(3.1415/4)-y*np.cos(3.1415/4)

print(x1)
print(y1)
print(z)               
