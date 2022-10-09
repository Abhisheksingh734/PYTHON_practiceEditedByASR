age1 = int(input("please enter your age:"))
age2 = int(input("please enter your age:"))
age3 = int(input("please enter your age:"))

if age1>age2>age3 :
    print ("first person is oldest")
elif age2>age1>age3 :
    print("second person is oldest")    
elif age3>age2>age1 :
    print ("third person is the oldest") 
else :
    print("all people are of same age")
   