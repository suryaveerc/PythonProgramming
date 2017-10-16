import turtle
import math


class Circle:
    def __init__(self,radius, width=1,color="white",outline="black"):
        self.radius = radius
        self.width = width
        self.color = color
        self.outline = outline
        
    def draw(self,turtle):
        centerX = turtle.xcor()
        centerY = turtle.ycor()
        turtle.penup()
        turtle.goto(centerX+self.radius,centerY)
        turtle.pendown()
        turtle.width(self.width)
        turtle.pencolor(self.outline)
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(361):
            newX = self.radius * math.cos((i/180.0) * math.pi) + centerX
            newY = self.radius * math.sin((i/180.0) * math.pi) + centerY
            turtle.goto(newX,newY)
            
        turtle.end_fill()
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.pendown()
        
def main():
    
    t = turtle.Turtle()
    t.ht()
    screen = t.getscreen()
    screen.tracer(0)
    
    for x in range(400):
        c = Circle(x/16+4,width=2,color="yellow")
        c.draw(t)
        # This angle is chosen because it is approx.
        # 360/1.61803399. The 1.61803399 is the approx.
        # value of the golden angle
        t.left(222.5)
        t.penup()
        t.forward(x*2 + 8)
        screen.update()
    
    
    
    screen.exitonclick()
    
if __name__ == "__main__":
    main()