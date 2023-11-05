import turtle
import math

pi = math.pi


briza = turtle.Turtle()
turtle.bgcolor('0,255,0')


print(briza)

def quadrado(t,largura):
    for i in range(largura):
        t.fd(100)
        t.lt(90)

def poligono(t,n,largura):
    angulo = 360 / n
    for i in range(n):
        t.fd(largura)
        t.lt(angulo)

def flor(t,n,largura):
    angulo = 300 / n
    for i in range(n):
        t.fd(largura)
        t.lt(angulo)

flor(briza,8,100)


turtle.mainloop()