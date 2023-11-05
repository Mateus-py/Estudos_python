import turtle

bob = turtle.Turtle()

print(bob)
def square(t,lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)

square(bob,200)
turtle.mainloop()