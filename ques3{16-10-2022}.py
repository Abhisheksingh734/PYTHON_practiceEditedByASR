#take input for first sec operator 
from ast import operator


num1=int(input("please input number1 :"))
num2 = int (input ("please input number 2 :"))
operatorr= str(input("please input operator:"))

if operatorr=="+":
    print(num1 + num2)
elif operatorr=="*":
    print(num1 * num2)
elif operatorr=="/":
    print(num1/num2)
elif operatorr=="-":
    print(num1 - num2)
else :
    print ("invalid data")



