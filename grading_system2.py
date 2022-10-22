x = int(input("please enter obtained marks :"))
y = int(input("please enter total marks :"))
z = (x/y)*100

print("your percentage is",z,"%")

if z>=33 and z<=50 :
    print("congratulations you PASSED the exam. and your grade is D")
elif z>50 and z<=75 :
    print("congratulations you PASSED the exam. and your grade is C")
elif z>75 and z<=90 :
    print("congratulations you PASSED the exam. and your grade is B")
elif z>90 and z<=100:
    print("congratulations you PASSED the exam. and your grade is A")
elif z<33 and z>= 0:
    print("you've failed the exam better luck next time")
else:
    print("invalid data :(")