import turtle as t

#========Question 1=========

t.shape("turtle")
t.color("green")
t.title("My turtle")

t.forward(100)
t.right(90)
t.backward(50)
t.circle(45)
t.hideturtle()
t.showturtle()
t.backward(50)
t.right(70)
t.forward(50)
t.goto(50,50)
t.penup()
t.pendown()
t.circle(45,steps=4)
t.color("blue")
t.pensize(3)


#=======Question 2========
t.goto(-200,-50)
t.pendown()
t.circle(40,steps=3)

t.penup()
t.goto(-100,-50)
t.pendown()
t.circle(40,steps=4)
t.done()
#===============Question 3=========
x1=int(input("Enter the value of x1  : "))
y1=int(input("Enter the value of y1 : "))
x2=int(input("Enter the value of the x2  : "))
y2=int(input("Enter the value of the  y2 : "))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
t.penup()
t.goto(x1,y1)
t.write("p1")
t.pendown()
t.goto(x2,y2)
t.write("p2")
t.penup()
t.goto((x1+x2)/2,(y1+y2)/2)
t.write(distance)
t.hideturtle()
t.done()



# ====Question 4=============
x1=int(input("Enter the value of x1  : "))
y1=int(input("Enter the value of y1 : "))
x2=int(input("Enter the value of the x2  : "))
y2=int(input("Enter the value of the  y2 : "))
x3=int(input("Enter Radius  : "))
distance=((x1-x2)**2+(y1-y2)**2)**0.5
t.pensize(3)
t.color("red")
t.penup()
t.goto(x1,y1)
t.pendown()
t.circle(x3)
t.penup()
t.goto(x2,y2)
t.begin_fill()
t.color("purple")
t.pendown()
t.circle(2)
t.goto(x2,y2+3)
t.write("p1")
t.end_fill()
t.penup()
t.goto(x1-x3,y1-x3)
if distance<=x3:
    t.write("P1 is inside the circle",font=("Times",18,"bold"))
else:
    t.write("P1 is the outside the circle ")
t.hideturtle()
# ====Question 5=======
t.pensize(5)

t.penup()
t.goto(-110,-25)
t.begin_fill()
t.color("blue")
t.pendown()
t.circle(40)
t.penup()
t.goto(0,-25)
t.begin_fill()
t.color("black")
t.pendown()
t.circle(40)
t.penup()
t.goto(110,-25)
t.begin_fill()
t.color("red")
t.pendown()
t.circle(40)
t.penup()
t.goto(-55,-75)
t.begin_fill()
t.color("yellow")
t.pendown()
t.circle(40)
t.penup()
t.goto(55,-75)
t.begin_fill()
t.color("green")
t.pendown()
t.circle(40)
# t.done()


#========Question 6========
class  Dog:
    a1="mamal"
    a2="dog"
    def fun(self):
        print("I am a ", self.a1)
        print("I am a ",self.a2)
AhsanAli=Dog()
print(AhsanAli.a1)
AhsanAli.fun()
class circle:
    x=10
    y=10
    radius=50
    def drawCircle(self):
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.circle(self.radius)
a=circle()
a.drawCircle()
t.done()

