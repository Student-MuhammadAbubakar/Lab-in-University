# #!=====Question 1=====
# class Student:
#     def __init__(self,marks):
#         self.marks=marks
#     def __add__(self,other):
#         return Student(self.marks + other.marks)
#     # def __str__(self):#dunder method for string representation of the object
#     #     return str(self.marks)
# s1=Student(80)  
# s2=Student(90)
# s3=Student(70)
# result=s1+s2+s3
# print(result.marks)
# #!=====Question 2=====
# class Add:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,other):
#      return self.a+other.a
# a1=Add(10)
# a2=Add(20)
# print(a1+a2)
# a3=Add("Lahore")
# a4=Add("pakistan")
# print(a3+a4)
# !#=====Question 3=====
# class Person:
#     def __init__(self,fname ,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class Student(Person):
#     pass
# x=Student("Muhammad ","Abubakar")
# x.printname()
#!========Question 4=====
# class Person:
#     def __init__(self,fname ,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(self.firstname,self.lastname)
# class Student(Person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         self.graduationyear=year
#     def welcome(self):
#         super().printname()
#         print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
# x=Student("Muhammad ","Abubakar",2024)
# x.welcome()
#!========Question 5=====
# class Person:
#     def __init__(self,fname ,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(self):
#         print(f"{self.firstname},{self.lastname}")
# class Student(Person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         self.graduationyear=year
#     def welcome(self):
#         super().printname()
#         print(f"Student Graduation Year: {self.graduationyear}")
# x=Student("Muhammad ","Abubakar",2024)
# x.welcome()
