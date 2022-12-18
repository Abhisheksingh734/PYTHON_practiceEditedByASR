import functools
list1 = [1,2,3,45,6,76,4,3,2,453,4355,35,25,34]
def Iseven(i):
    return i%2==0
output = list(filter(Iseven,list1))
print(output)
output2 = list(filter(lambda i:i>15,list1))
print(output2)

#map function
output3 = list(map(lambda i:i**2,list1))
print(output3)

output4 = functools.reduce(lambda a,b:a**b,list1)
print(output4)