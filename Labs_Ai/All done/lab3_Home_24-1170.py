import turtle as t
import math
#=====Question 1=======
x=int(input("Enter the value of x : "))
y=int(input("Enter the value of y : "))

t.forward(x)
t.left(90)
t.forward(y)
t.left(90)
t.forward(x)
t.left(90) 
t.forward(y)
t.left(90) 
#=======Question 2=========
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
#====Question 3=========
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
r1 = int(input("Enter radius1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
r2 = int(input("Enter radius2: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

t.speed(0)

t.penup()
t.goto(x1, y1-r1)
t.pendown()
t.color("red")
t.circle(r1)

t.penup()
t.goto(x2, y2-r2)
t.pendown()
t.color("blue")
t.circle(r2)


t.penup()
t.goto(-200, 200)

if distance + r2 <= r1:
    t.write("Circle2 is inside Circle1", font=("Arial",16,"bold"))

elif distance <= r1 + r2:
    t.write("Circle2 overlaps Circle1", font=("Arial",16,"bold"))

else:
    t.write("No Overlap", font=("Arial",16,"bold"))

t.hideturtle()
t.done()
#=====Question 4=========
class Book:

    def __init__(self, isbn, title, price, main, sub, pages):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.main = main
        self.sub = sub
        self.pages = pages

    def display(self):
        print("ISBN:", self.isbn)
        print("Title:", self.title)
        print("Price:", self.price)
        print("Main Area:", self.main)
        print("Sub Area:", self.sub)
        print("Pages:", self.pages)



b1 = Book("12345","Python Book",500,"CS","Programming",300)


b1.display()
#======Question 5=========
class Computer:

    def __init__(self, brand, speed, memory):
        self.brand = brand
        self.speed = speed
        self.memory = memory

    def display(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)
        print("Memory:", self.memory)



c1 = Computer("HP",3.2,8)


c1.display()
class Loan:

    def __init__(self):
        self.annualInterestRate = 2.5
        self.numberOfYears = 1
        self.loanAmount = 1000
        self.borrower = " "

    def getMonthlyPayment(self):
        monthlyInterestRate = self.annualInterestRate / 1200
        monthlyPayment = self.loanAmount * monthlyInterestRate / \
            (1 - (1 + monthlyInterestRate) ** (-self.numberOfYears * 12))
        return monthlyPayment

    def getTotalPayment(self):
        totalPayment = self.getMonthlyPayment() * self.numberOfYears * 12
        return totalPayment

    def display(self):
        print("----- Loan Details -----")
        print("Borrower:", self.borrower)
        print("Loan Amount:", self.loanAmount)
        print("Annual Interest Rate:", self.annualInterestRate)
        print("Number of Years:", self.numberOfYears)
        print("Monthly Payment:", round(self.getMonthlyPayment(), 2))
        print("Total Payment:", round(self.getTotalPayment(), 2))
        print("------------------------")



myLoan = Loan() 
myLoan.borrower = "Muhammad Abubakar"
myLoan.loanAmount = 5000
myLoan.annualInterestRate = 3.5
myLoan.numberOfYears = 5


myLoan.display()
#===Question 7========

class BMI:

    def __init__(self, name, age, weight, height):

        self.name = name
        self.age = age
        self.weight = weight      
        self.height = height      


    def getBMI(self):

        bmi = self.weight / (self.height * self.height)

        return bmi
    def getStatus(self):

        bmi = self.getBMI()

        if bmi < 18.5:
            return "Underweight"

        elif bmi < 25:
            return "Normal"

        elif bmi < 30:
            return "Overweight"

        else:
            return "Obese"


    def display(self):

        print("Name:", self.name)
        print("Age:", self.age)
        print("Weight:", self.weight, "kg")
        print("Height:", self.height, "m")

        print("BMI:", round(self.getBMI(),2))
        print("Status:", self.getStatus())

bmi1 = BMI("Ahmed", 20, 70, 1.75)
bmi1.display()