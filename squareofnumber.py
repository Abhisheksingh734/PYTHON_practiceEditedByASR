def sqr(x): #wecan write this one line functions in another way aswell (using anonymous functions)called lambda func
    return x**2
sqr(5)

# also written as 
a = lambda x:x**2
product = a(7)

print(product)
# more than 2 parameters can also be defined 
a = lambda x,y:x*y
ans = a(5,4)
print(ans)