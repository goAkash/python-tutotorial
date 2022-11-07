# draw a ninja
import turtle
ninja =turtle.turtle()
ninja.speed(10)

for i in range(100):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.steposition(0) 
    ninja.pendown()

    ninja.right(2)
    turtle.done()