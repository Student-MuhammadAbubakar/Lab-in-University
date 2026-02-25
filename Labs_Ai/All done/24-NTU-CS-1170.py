#=====Example 1====
x=9
if x>0:
    if x>10:
        print("large")
    print("postive")
print("Done")
#===example 2====
y=20
if y>0:
    if y>10:
        print("large")
    print("postive")
print("Done")
#=======Example 3==========

x="Hello World"
y=20
a=20.5
x=1j
list=["Ali",20,20,"Rahman"]
tuple=("Apple",20,20,"cherry")
set={"Apple",21,20.5,20.5,"Ali"}

print(f"the value of the x is {x}\nThe value of list is {list}\nThe value of the tuple {tuple}\nThe value of the set is {set}\n")
#=======Example 4========
age=25
salery=145.5
name="John"
i,j,k="Orange","banana","Cherry"
print(f"Age is {age}\nSalery is {salery}\nname is {name}\n Value of i j and k is {i} {j} {k}")

a=int(input("Enter the value of a"))
print(f"The value of a is {a}")
print("Sum is ",a+a)
#==example 5=======
x="Muhammad Abubakar"
print("Index String",x[-8:-1])
print("Index String",x[:8])
print("Index String",x[9:])
print("Index String",x[9:-1])
#=======Example 6=====
a=60
b=13
print("a=",bin(a) ,"\n b=",bin(b))
print(bin(a&b))
#====example 7==========
a=int(input("Enter the value of a"))
if a==10:
    print("a is 10")
elif a==11:
    print("b is 11")
else:
    print("a is not present")

#===Example 8=======
def Add(x,y,z=0):
    print(f"The addition is {x+y+z}\n")
def Multiplication(x,y,z=1):
    print(f"The Multiplcation is {x*y*z}\n")
def Division(x,y,z=1):
    print(f"The division is {x//y//z}\n")

a=12.0
b=14.0
c=16.0
Add(a,b)
Add(a,b,c)
Multiplication(a,b)
Multiplication(a,b,c)
Division(a,b)
Division(a,b,c)

