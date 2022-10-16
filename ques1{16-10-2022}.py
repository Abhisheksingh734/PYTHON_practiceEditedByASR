#input divisible by both 3 and 2 
num = int(input("please enter number"))

if num % 2 == 0 and num % 3 == 0 :
    print("the number is divisible by both 2 and 3")
elif num % 2 == 0 and num % 3 != 0:
    print ("the number is only divisible by 2")
elif num % 3 == 0 and num % 2 != 0:
    print ("the number is only divisible by 3")
else :
    print ("invalid data")