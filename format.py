a = 5 
string = "value of a is ={} "#{}is a place holder
print(string.format(a))

#EXAMPLE2
a = 10
b = 22
c =98
string = "A = {} B = {} C = {}"
print(string.format(a,b,c))

#EXAMPLE 3
a = 10
b = 22
c =98
string = "A = {0} B = {2} C = {1}" #we can put index inside place holder to make values shuffle as shown
print(string.format(a,b,c))