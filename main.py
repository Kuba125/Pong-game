import turtle as t
t = t.Turtle()

window = t.screen
window.title("Pong")
window.setup(width=1000, height=600)
window.bgcolor("black")

HIGH_BORDER = 200
LOW_BORDER = -200
PADDLE_MOVEMENT = 30

t.lt(90)
t.color("white")
t.shape("square")
t.shapesize(1,7)
print(t.pos())
t.penup()

def up():
    if t.pos()[1] > HIGH_BORDER:
        pass
    else:
        t.fd(PADDLE_MOVEMENT)

def down():
    if t.pos()[1] < LOW_BORDER:
        pass
    else:
        t.bk(PADDLE_MOVEMENT)


t.goto(400,0)

window.onkeypress(up, 'w')
window.onkeypress(down, 's')



def wyglad():
    t.pensize(5)

window.listen()
window.mainloop()