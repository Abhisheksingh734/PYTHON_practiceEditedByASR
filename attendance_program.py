total_lectures=int(input("enter the total no. of lectures:"))
attended_lectures = int(input("enter the total no. of lectures you have attended:"))
eligibility_base = (attended_lectures/total_lectures)*100
if eligibility_base>=75:
    print("congratulations you are eligible for examinations and your current attendance percenttage is :", eligibility_base)
else:
    print("you can go home :), your current attendace percentage is",eligibility_base )    