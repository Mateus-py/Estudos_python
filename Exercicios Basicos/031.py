import turtle
import math


bob = turtle.Turtle()


print(bob)

def quadrado(t,length):
    for i in range(0,4):
        t.fd(length)
        t.lt(90)

def poligono(t , n ,length):
    angulo = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angulo)

def circulo(t,r):
    circuferencia = 2 * math.pi * r
    n = 50
    length = circuferencia / n

poligono(bob,100,5)

turtle.mainloop()