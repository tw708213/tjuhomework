
from tracemalloc import stop
import turtle

def drawsnake():
    turtle.goto(-300,100)
    turtle.pendown()
    turtle.fd(600)
    turtle.fd(-300)
    turtle.seth(70)
    turtle.circle(700,20)
    turtle.seth(270)
    turtle.circle(-700,60)
    turtle.seth(30)
    turtle.circle(700,40)
    turtle.seth(-70)
    turtle.circle(600,50)
    
def dazi_main():
    turtle.setup(1300,800,0,0)
    turtle.pensize(20)
    turtle.speed(10)
    turtle.pencolor("red")
    turtle.penup()
    turtle.seth(0)
    drawsnake()
    turtle.done()
