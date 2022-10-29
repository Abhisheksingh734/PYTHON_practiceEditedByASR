age = int(input("please enter your age passanger 1 :"))
gender = str(input("please enter your gender passanger 1 :"))
age2 = int(input("please enter your age passanger 2 :")) 
gender2 = str(input("please enter your gender passanger 2 :"))

if age>age2 and gender=="female" and  gender2=="female":
    print("passanger 1 will get the lower berth")
elif age>age2 and gender == "male" and gender2 =="male":
    print("passanger 1 will get the lower berth")
elif age>age2 and gender == "male" and gender2 =="female"  and age >= 60:
    print("passanger 1 will get the lower berth")
elif age>age2 and gender == "male" and gender2 =="female" and age<=60:
    print("passanger 2 will get the lower berth")
elif age2>age and gender=="female" and  gender2=="female":
    print("passanger 2 will get the lower berth")
elif age2>age and gender == "male" and gender2 =="male":
    print("passanger 2 will get the lower berth")
elif age2>age and gender == "male" and gender2 =="female"  and age >= 60:
    print("passanger 2 will get the lower berth")
elif age2>age and gender == "male" and gender2 =="female" and age<=60:
    print("passanger 1 will get the lower berth")
else :
    print("invalid data")
