from turtle import Screen, Turtle
from paddle import Paddle

paddle_1 = Paddle('right')
paddle_2 = Paddle('left')

window = Screen()
window.title("Pong")
window.setup(width=1000, height=600)
window.bgcolor("black")



window.onkeypress(paddle_1.up, 'w')
window.onkeypress(paddle_1.down, 's')

window.onkeypress(paddle_2.up, 'Up')
window.onkeypress(paddle_2.down, 'Down')


window.listen()
window.mainloop()