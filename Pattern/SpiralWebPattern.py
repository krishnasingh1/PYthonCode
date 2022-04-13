import turtle

colors = ['red', 'magenta', 'blue', 'cyan', 'green', 'white']

t = turtle.Pen()

t.speed(100000)

turtle.bgcolor('black')

for x in range(200):
    t.pencolor(colors[x % 6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)

turtle.down()
