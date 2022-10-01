x = input("enter num1:")
y = input("enter num2:")
temp = x #in this line of code we took a variable temp to assign its value as of x 
x = y #then we overwrite the value of x as y
y = temp #now we use the older temp value and assign it as y
print("after swapping value of num1 is :", x)
print ("after swapping value of num2 is :",y)