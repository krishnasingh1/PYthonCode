from turtle import*

speed(11)
hideturtle()
color('blue')
bgcolor('black')
p = True
n = 1
while True :
    circle(n)
    if p:
        n = n - 1
    else:
        n = n + 1

    if n == 0 or n == 60 :
        p = not p
    left(1)
    forward(3)


