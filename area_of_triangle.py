side1 = float(input("enter the lenght of first side:"))
side2 = float(input("enter the length of second side:"))
side3 = float(input("enter the length of third side:"))
semiperimeter = (side1 + side2 + side3)/2
area = (semiperimeter*(semiperimeter-side1)*(semiperimeter-side2)*(semiperimeter-side3))
print(area)