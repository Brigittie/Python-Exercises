import turtle

speed = 10

def square(x,y,z):
    turtle.pensize(10)
    turtle.pencolor("orange")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(z)
    turtle.right(90)
    turtle.forward(z)
    turtle.right(90)
    turtle.forward(z)
    turtle.right(90)
    turtle.forward(z)


def colorSquare(a,b,c):
    turtle.pensize(5)
    turtle.pencolor("green")
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(c)
    turtle.right(90)
    turtle.forward(c)
    turtle.right(90)
    turtle.forward(c)
    turtle.right(90)
    turtle.forward(c)
#start off with these variables

x = 150
y = 150
z = 400
a = 125
b = 125
c = 350

#creating 4 main square sections
#while square is greater than 0 pixels, draw square
#then take the size of the square, divide by 4 and make the pensize 2x smaller
#continue drawing square until
#else print finito


#turtle.pensize(b)

while ((z > 0) and (c > 0)):
    square(x, y, z)
    x = x-37.5
    y = y-37.5
    z = z-80
    colorSquare(a,b,c)
    a = a-18.75
    b = b-18.75
    c = c-40
else:
    print("finito!")
    #turtle.pensize(b-4)




#creating subdivision sections



turtle.mainloop() 
