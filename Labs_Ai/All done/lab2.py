#===Quetion 1===
def conversion():
    C=float(input("Enter the number in celsius : "))
    farenhit=(9/5)*C+32
    print(f"The temperture if celcius {C} is {farenhit} in Farenhit")
conversion()
 
#======Question 2=======
def Area():
    radius=float(input("Enter the radius : "))
    length=float(input("Enter the length : "))
    area=radius*radius*3.14
    volume=area*length
    print(f"The area of the cylinder is {area} and its volume is {volume}")
Area()
 #=======Question 3=======   
def feettometer():
    feet=float(input("Enter the no of feet to be converted in meter : "))
    meter=feet*0.305
    print(f"The pound in kilograms are {meter} ")
feettometer()
    
#======Question 4=======
def pound():
    pound=float(input("Enter the pound to be converted : "))
    kilogram=pound*0.454
    print(f"The pound in kilograms are {kilogram} ")
pound()

#======Question 5=======
def Calculation():
    subtotal=float(input("Enter the subtotal : "))
    gratuity=float(input("Enter the gratuity : "))
    Gratuit=gratuity*(15/100)
    total=subtotal+Gratuit
    print(f" The gratuity is {Gratuit} and the Total is {total}")
Calculation()

#======Question 8=======
def Calmeter():
    mile=float(input("Enter the number in miles : "))
    kilometer=mile*0.6215
    print(f"The number of kilometer in miles {mile} are {kilometer}")
Calmeter()
 #======Question 8=======
def Calmeter():
    mile=float(input("Enter the number in miles : "))
    kilometer=mile*0.6215
    print(f"The number of kilometer in miles {mile} are {kilometer}")
Calmeter()
#======Question 6=======
name=input("enter the employees name : ")
hours=int(input("Enter the number of hours work in a week : "))
hourlypay=int(input("enter the hourly pay rate : "))
grosspay=int(input("Enter the gross pay : "))
fwithholdinrate=float(input("Enter the federal withholding rate: "))
staterate=float(input("Enter the state withholding rate: "))
federal=(grosspay*(fwithholdinrate/100))
state=(grosspay*(staterate/100))
totaldetection=federal+state
netpay=(grosspay-federal)-state
print(f"The name is {name}\nfederal withdrawing is {federal}\nSTate withdrawing is {state}\nThe total detection is {totaldetection}\n THe net pay is {netpay}")

#======Question 7=======
def Invester():
    amount=int(input("Enter the amount "))
    rate=float(input("Enter the interest rate : "))
    year=int(input("Enter the year : "))
    futureinvester=amount*(1+(rate/100)*(year*12))
    print(f"The Future invester rate is {futureinvester}")
Invester()     

