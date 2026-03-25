#!====================Question 1==================
# t=float(input("Enter the temperature degree in Calcius: "))
# forenheit=(9/5)*t+32
# print(F"{t} degree in Calcius is {forenheit} degree in Forenheit")
#!====================Question 2==================
# radius=float(input("Enter the radius of the cylinder: "))
# length=float(input("Enter the length of the cylinder: "))
# Area=radius*radius*3.14
# Volume=Area*length
# print(f"The area of the cylinder is {Area}\nThe volume of the cylinder is {Volume}  ")
#!====================Question 3==================
# name=input("Enter Employee  name: ")
# hours=float(input("Enter the number of hours worked : "))
# hourly_rate=float(input("Enter the hourly pay rate: "))
# federal_tax=float(input("Enter the federal tax rate: "))
# State_tax=float(input("Enter the state tax rate: "))
# gross_pay=hours*hourly_rate
# deduction=gross_pay*hourly_rate
# Total_deduction=federal_tax+State_tax
# net_pay=gross_pay-Total_deduction
# print(f"Employee Name: {name}\nHours Worked: {hours}\nPay Rate: {hourly_rate}\nGross Pay: {gross_pay}\nDeductions: {deduction}\nNet Pay: {net_pay}")
#!====================Question 4==================
# amount=float(input("Enter the amount of money: "))
# interest_rate=float(input("Enter the annual interest rate: "))
# number_of_years=float(input("Enter the number of years: "))
# Monthly_interest_rate=interest_rate/1200
# Futurevalue=amount*((1+Monthly_interest_rate)**(number_of_years*12))
# print(f"The Accumulated value is {Futurevalue:.2f}")
#!====================Question 5==================
# import turtle

# x = float(input("Enter point x: "))
# y = float(input("Enter point y: "))

# radius = 10
# width = 10
# height = 5

# scale = 20

# screen = turtle.Screen()

# pen = turtle.Turtle()
# pen.hideturtle()
# pen.speed(0)
# pen.pensize(2)

# pen.penup()
# pen.goto(0, -radius * scale)
# pen.pendown()
# pen.pencolor("red")
# pen.circle(radius * scale)

# left = -(width / 2) * scale
# right = (width / 2) * scale
# top = (height / 2) * scale
# bottom = -(height / 2) * scale

# pen.penup()
# pen.goto(left, top)
# pen.pendown()
# pen.pencolor("blue")
# pen.goto(right, top)
# pen.goto(right, bottom)
# pen.goto(left, bottom)
# pen.goto(left, top)

# if x*2 + y*2 < radius*2:
# 	circle_result = f"Point ({x:g}, {y:g}) is inside the circle."
# else:
# 	circle_result = f"Point ({x:g}, {y:g}) is outside the circle."

# if abs(x) <= width / 2 and abs(y) <= height / 2:
# 	rectangle_result = f"Point ({x:g}, {y:g}) is inside the rectangle."
# else:
# 	rectangle_result = f"Point ({x:g}, {y:g}) is outside the rectangle."

# pen.penup()
# pen.goto(x * scale, y * scale)
# pen.dot(10, "black")
# pen.goto(x * scale + 8, y * scale + 8)
# pen.pencolor("black")
# pen.write(f"({x:g}, {y:g})")

# pen.goto(x * scale + 8, y * scale - 12)
# pen.write(circle_result)
# pen.goto(x * scale + 8, y * scale - 30)
# pen.write(rectangle_result)

# turtle.done()
#!====================Question 6==================
# class Book:
#     def __init__(self,ISBN,Title,Price,mainArea,SubArea,Noofpages):
#         self.ISBN=ISBN
#         self.Title=Title
#         self.Price=Price
#         self.mainArea=mainArea
#         self.SubArea=SubArea
#         self.Noofpages=Noofpages
#     def display(self):
#         print(f"ISBN: {self.ISBN}\nTitle: {self.Title}\nPrice: Rs.{self.Price}\nMain Area: {self.mainArea}\nSub Area: {self.SubArea}\nNumber of Pages: {self.Noofpages}\n\n=======================\n\n")
# Book1=Book("978-0134610997","Intro to python",45,"Computer Science","Programming",850)
# Book2=Book("978-0134190440","Data Structures and Algorithm",50,"Computer Science","Programming",1200)
# Book1.display()
# Book2.display()
#!====================Question 7==================


# class Loan:
#     def __init__(
#         self, annual_interest_rate=2.5, number_of_years=1, loan_amount=1000, Borrower=""
#     ):
#         self.__annual_interest_rate = annual_interest_rate
#         self.__number_of_years = number_of_years
#         self.__loan_amount = loan_amount
#         self.__Borrower = Borrower

#     def get_monthly_payment(self):
#         monthly_interest_rate = self.__annual_interest_rate / 1200
#         monthly_payment = (
#             self.__loan_amount
#             * monthly_interest_rate
#             / (1 - 1 / (1 + monthly_interest_rate) ** (self.__number_of_years * 12))
#         )
#         return monthly_payment

#     def set_get_monthly_payment(self, monthly_payment):
#         self.__monthly_payment = monthly_payment

#     def get_annual_interest_rate(self):
#         return self.__annual_interest_rate

#     def set_annual_interest_rate(self, annual_interest_rate):
#         self.__annual_interest_rate = annual_interest_rate

#     def get_loan_amount(self):
#         return self.__loan_amount

#     def set_loan_amount(self, loan_amount):
#         self.__loan_amount = loan_amount

#     def get_total_payment(self):
#         total_payment = self.get_monthly_payment() * self.__number_of_years * 12
#         return total_payment

#     def set_total_payment(self, total_payment):
#         self.__total_payment = total_payment

#     def get_Number_of_years(self):
#         return self.__number_of_years

#     def set_Number_of_years(self, number_of_years):
#         self.__number_of_years = number_of_years

#     def get_Borrower(self):
#         return self.__Borrower

#     def set_Borrower(self, borrower):
#         self.__Borrower = borrower


# loan1 = Loan(5.5, 15, 250000, "John Doe")
# print(
#     f"Loan Details:\nBorrower: {loan1.get_Borrower()}\nAnnual Interest Rate: {loan1.get_annual_interest_rate()}%\nNumber of Years: {loan1.get_Number_of_years()}\nLoan Amount: Rs.{loan1.get_loan_amount()}\nMonthly Payment: Rs.{loan1.get_monthly_payment()}\nTotal Payment: Rs.{loan1.get_total_payment():.2f}"
# )
#!==============Question 8==================
# class  BMI:
#     def __init__(self,name,age,weight,height):
#         self.__name=name
#         self.__age=age
#         self.__weight=weight
#         self.__height=height
#     def get_name(self):
#         return self.__name
#     def get_age(self):
#         return self.__age
#     def get_weight(self):
#         return self.__weight
#     def get_height(self):
#         return self.__height
#     def get_BMI(self):
#         return (self.__weight/self.__height)**2
#     def getstatus(self):
#         bmi=self.get_BMI()
#         if(bmi<18.5):
#             print("UnderWeight")
#         elif (bmi < 25):
#             return "Normal"
#         elif (bmi < 30):
#             return "Overweight"
#         else:
#             return "Obese"
#     def Display(self):
#         print(f"Name is {self.get_name()}\nBMI:{self.get_BMI()}\nStatus:{self.getstatus()}")
# Person1=BMI("Ayan",22,49.5,5.5)
# Person1.Display()
#!============+Question 9===========
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)

#     def __mul__(self, other):
#         return Complex((self.real * other.real) - (self.imag * other.imag), (self.real * other.imag) + (self.imag * other.real))

#     def __truediv__(self, other):
#         denominator = (other.real * other.real) + (other.imag * other.imag)
#         return Complex(((self.real * other.real) + (self.imag * other.imag)) / denominator, ((self.imag * other.real) - (self.real * other.imag)) / denominator)

#     def __str__(self):
#         return str(self.real) + " + " + str(self.imag) + "i" if self.imag >= 0 else str(self.real) + " - " + str(abs(self.imag)) + "i"


# c1 = Complex(4, 3)
# c2 = Complex(2, 1)

# print("c1 =", c1)
# print("c2 =", c2)
# print()
# print("c1 - c2 =", c1 - c2)
# print("c1 * c2 =", c1 * c2)
# print("c1 / c2 =", c1 / c2)
