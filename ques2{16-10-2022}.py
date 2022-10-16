# take user input 3 sides of triangle to check if its possible to form a triangle
side1 = int(input("please enter length of side 1:"))
side2 = int(input("please enter length of side 2:"))
side3 = int(input("please enter length of side 3:"))

if side1<side2+side3 and side2<side1+side3  and side3 < side2+side1:
    print("triangle is possible")
else :
    print("triangle is not  possible")