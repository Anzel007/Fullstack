# creating a calculator
import math
class Calculator:
    # def __init__(self):
    #     pass
    def add(self,a,b):
        return(a+b)
    def subtract(self,a,b):
        return(a-b)
    def multiply(self,a,b):
        return(a*b)
    def division(self,a,b):
        try:
            return(a/b)
        except: 
            return("error")
    def sine(self,a):
        return(math.sin(math.radians(a)))
    def square_root(self,a):
        try:
            return(math.sqrt(a))
        except:
            return("error")
    def log(self,a):
        try:
            return(math.log(a))
        except:
            return("error")



C= Calculator()
while True:
    a= float(input("enter first number"))
    b= float(input("enter second number"))

    s=input('''enter the symbol for calculation  +  -  *  / 
            '1' for square root,
            '2' for sine function of 1st number,, 
            '3' to find logarithmic function of the number \n''')



    if s=="+":
        print("the result is",C.add(a,b))
    elif s=="-":
        print("the result is",C.subtract(a,b))
    
    elif s=="*":
        print("the result is",C.multiply(a,b))
    
    elif s=="/":
        print("the result is",C.division(a,b))
    
    elif s=="1":
        print("the result is",C.square_root(a))
    
    elif s=="2":
        print("the result is",C.sine(a))
    
    elif s=="3":
        print("the result is",C.log(a))


    choice= input("do you want to conmtinue?  (y/n) ---> ")

    if choice=="n":
        print("exiting program")
        break


    
