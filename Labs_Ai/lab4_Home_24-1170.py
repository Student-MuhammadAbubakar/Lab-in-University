# #! ==========Question 1==========
# class Loan:
#     def __init__(self):
#         self.__annualInterestRate = 2.5
#         self.__numberOfYears = 1
#         self.__loanAmount = 1000
#         self.__borrower = ""


#     def getAnnualInterestRate(self):
#         return self.__annualInterestRate

#     def getNumberOfYears(self):
#         return self.__numberOfYears

#     def getLoanAmount(self):
#         return self.__loanAmount

#     def getBorrower(self):
#         return self.__borrower


#     def setAnnualInterestRate(self, annualInterestRate):
#         self.__annualInterestRate = annualInterestRate

#     def setNumberOfYears(self, numberOfYears):
#         self.__numberOfYears = numberOfYears

#     def setLoanAmount(self, loanAmount):
#         self.__loanAmount = loanAmount

#     def setBorrower(self, borrower):
#         self.__borrower = borrower



#     def getMonthlyPayment(self):
#         monthlyInterestRate = self.__annualInterestRate / 1200
#         monthlyPayment = (
#             self.__loanAmount * monthlyInterestRate
#         ) / (
#             1 - (1 / (1 + monthlyInterestRate) ** (self.__numberOfYears * 12))
#         )

#         return monthlyPayment

#     def getTotalPayment(self):

#         totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12

#         return totalPayment
#     def display(self):

#         print("------ Loan Information ------")
#         print("Borrower Name   :", self.__borrower)
#         print("Interest Rate   :", self.__annualInterestRate, "%")
#         print("Loan Years      :", self.__numberOfYears)
#         print("Loan Amount     :", self.__loanAmount)
#         print("Monthly Payment :", self.getMonthlyPayment())
#         print("Total Payment   :", self.getTotalPayment())
#         print("------------------------------")

# loan=Loan()
# loan.setBorrower("John Doe")
# loan.setAnnualInterestRate(3.5)
# loan.setNumberOfYears(5)    
# loan.setLoanAmount(20000)
# loan.display()
# #! ==========Question 2==========
# class BMI:

    
#     def __init__(self, name, age, weight, height):

#         self.__name = name
#         self.__age = age
#         self.__weight = weight    
#         self.__height = height   


#     def getName(self):
#         return self.__name

#     def getAge(self):
#         return self.__age

#     def getWeight(self):
#         return self.__weight

#     def getHeight(self):
#         return self.__height

#     def getBMI(self):

#         bmi = self.__weight / (self.__height ** 2)

#         return round(bmi, 2)
#     def getStatus(self):

#         bmi = self.getBMI()

#         if bmi < 18.5:
#             return "Underweight"

#         elif bmi < 25:
#             return "Normal"

#         elif bmi < 30:
#             return "Overweight"

#         else:
#             return "Obese"
        
#     def display(self):

#         print("------ BMI Information ------")
#         print("Name   :", self.__name)
#         print("Age    :", self.__age)
#         print("Weight :", self.__weight, "kg")
#         print("Height :", self.__height, "m")
#         print("BMI    :", self.getBMI())
#         print("Status :", self.getStatus())
    
# person=BMI("Alice", 30, 68, 1.65)
# person.display()   
# #! ==========Question 3==========
# class Complex:

#     def __init__(self, real, imag):

#         self.__real = real
#         self.__imag = imag

#     def display(self):

#         if self.__imag >= 0:
#             print(f"{self.__real} + {self.__imag}i")
#         else:
#             print(f"{self.__real} - {abs(self.__imag)}i")
#     def __sub__(self, other):

#         real = self.__real - other.__real
#         imag = self.__imag - other.__imag

#         return Complex(real, imag)
#     def __mul__(self, other):

#         real = (self.__real * other.__real) - (self.__imag * other.__imag)
#         imag = (self.__real * other.__imag) + (self.__imag * other.__real)

#         return Complex(real, imag)
#     def __truediv__(self, other):

#         denominator = (other.__real ** 2) + (other.__imag ** 2)

#         real = (
#             (self.__real * other.__real) + (self.__imag * other.__imag)
#         ) / denominator

#         imag = (
#             (self.__imag * other.__real) - (self.__real * other.__imag)
#         ) / denominator

#         return Complex(real, imag)

# c1 = Complex(4, 3)   
# c2 = Complex(2, 1)   
# result1 = c1 - c2
# print("Subtraction:")
# result1.display()
# result2 = c1 * c2
# print("Multiplication:")
# result2.display()

# result3 = c1 / c2
# print("Division:")
# result3.display()
##! ==========Question 4==========
# id="rn001"
# class RationalNumber:
#     def __init__(self, numerator, denominator):

#         if denominator == 0:
#             raise ValueError("Denominator cannot be zero")
#         if denominator < 0:
#             numerator = -numerator
#             denominator = -denominator
#         gcd = self.__gcd(abs(numerator), abs(denominator))

#         self.__num = numerator // gcd
#         self.__den = denominator // gcd

#     def __gcd(self, a, b):

#         while b != 0:
#             a, b = b, a % b

#         return a
#     def __str__(self):
#         return f"{self.__num}/{self.__den}"
#     def __add__(self, other):
#         num = self.__num * other.__den + other.__num * self.__den
#         den = self.__den * other.__den
#         return RationalNumber(num, den)
#     def __sub__(self, other):
#         num = self.__num * other.__den - other.__num * self.__den
#         den = self.__den * other.__den
#         return RationalNumber(num, den)
#     def __mul__(self, other):
#         num = self.__num * other.__num
#         den = self.__den * other.__den

#         return RationalNumber(num, den)
#     def __truediv__(self, other):

#         if other.__num == 0:
#             raise ValueError("Cannot divide by zero")

#         num = self.__num * other.__den
#         den = self.__den * other.__num

#         return RationalNumber(num, den)
#     def __eq__(self, other):
#         return self.__num == other.__num and self.__den == other.__den


#     def __lt__(self, other):
#         return self.__num * other.__den < other.__num * self.__den


#     def __le__(self, other):
#         return self.__num * other.__den <= other.__num * self.__den


#     def __gt__(self, other):
#         return self.__num * other.__den > other.__num * self.__den


#     def __ge__(self, other):
#         return self.__num * other.__den >= other.__num * self.__den
    
# r1 = RationalNumber(1, 2)
# r2 = RationalNumber(3, 4)   
# print("R1:", r1)
# print("R2:", r2)
# print("R1 + R2:", r1 + r2)
# print("R1 - R2:", r1 - r2)
# print("R1 * R2:", r1 * r2)
# print("R1 / R2:", r1 / r2)
# print("R1 == R2:", r1 == r2)
# print("R1 < R2:", r1 < r2)
# print("R1 <= R2:", r1 <= r2)
# print("R1 > R2:", r1 > r2)
# print("R1 >= R2:", r1 >= r2)
#! ==========Question 5==========
# id="poly001"
# class Polynomial:
#     def __init__(self, terms=None):

#         if terms is None:
#             self.__terms = []
#         else:
#             self.__terms = terms.copy()

#         self.__simplify()
#     def __simplify(self):

#         temp = {}

#         for coef, exp in self.__terms:

#             if exp in temp:
#                 temp[exp] += coef
#             else:
#                 temp[exp] = coef

#         self.__terms = []

#         for exp, coef in temp.items():

#             if coef != 0:
#                 self.__terms.append((coef, exp))

#         self.__terms.sort(key=lambda x: x[1], reverse=True)

#     def __str__(self):

#         if not self.__terms:
#             return "0"

#         result = []

#         for coef, exp in self.__terms:

#             if exp == 0:
#                 result.append(str(coef))

#             elif exp == 1:
#                 result.append(f"{coef}x")

#             else:
#                 result.append(f"{coef}x^{exp}")

#         return " + ".join(result)

#     def getTerms(self):
#         return self.__terms.copy()

#     def __assign__(self, other):

#         self.__terms = other.__terms.copy()
#     def __add__(self, other):

#         return Polynomial(self.__terms + other.__terms)

#     def __sub__(self, other):

#         new_terms = self.__terms.copy()

#         for coef, exp in other.__terms:
#             new_terms.append((-coef, exp))

#         return Polynomial(new_terms)
#     def __mul__(self, other):

#         result = []

#         for c1, e1 in self.__terms:
#             for c2, e2 in other.__terms:

#                 result.append(
#                     (c1 * c2, e1 + e2)
#                 )

#         return Polynomial(result)
#     def __iadd__(self, other):

#         self.__terms += other.__terms
#         self.__simplify()

#         return self
#     def __isub__(self, other):

#         for coef, exp in other.__terms:
#             self.__terms.append((-coef, exp))

#         self.__simplify()

#         return self
#     def __imul__(self, other):

#         result = []

#         for c1, e1 in self.__terms:
#             for c2, e2 in other.__terms:
#                 result.append((c1 * c2, e1 + e2))

#         self.__terms = result
#         self.__simplify()

#         return self
# p1 = Polynomial([(2, 3), (3, 2), (4, 0)])
# p2 = Polynomial([(1, 2), (5, 1), (6, 0)])
# print("P1:", p1)
# print("P2:", p2)
# print("P1 + P2:", p1 + p2)
# print("P1 - P2:", p1 - p2)
# print("P1 * P2:", p1 * p2)
# p1 += p2
# print("P1 += P2:", p1)
# p1 -= p2
# print("P1 -= P2:", p1)

# p1 *= p2
# print("P1 *= P2:", p1)

