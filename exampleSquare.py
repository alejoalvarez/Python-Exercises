import turtle

window = turtle.Screen()
alejo = turtle.Turtle()
alejo.forward(50)
alejo.left(90)
alejo.forward(50)
alejo.left(90)
alejo.forward(50)
alejo.left(90)
alejo.forward(50)
alejo.left(90)



colors=['red','purple','blue','green','yellow','orange']

t = turtle.Pen()
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

# keep open turtle screen
turtle.mainloop()