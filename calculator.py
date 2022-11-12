n1 = int(input())
n2 = int(input())
op = str(input())

def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def div(num1,num2):
    print(num1/num2)
def mult(num1,num2):
    print(num1*num2)
if op == "+":
    add(n1,n2)
elif op == "*":
    mult(n1,n2)
elif op == "-":
    sub(n1,n2)
elif op == "/":
    div(n1,n2)
else :
    print("invalid data")