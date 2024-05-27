import turtle as t
t = t.Turtle()

window = t.screen
window.title("Pong")
window.setup(width=1000, height=600)
window.bgcolor("black")

t.color("white")
t.shape("square")
t.shapesize(7,1)
print(t.pos())
t.penup()

def up():
    t.fd(30)


t.goto(400,0)




def wyglad():
    t.pensize(5)


window.mainloop()