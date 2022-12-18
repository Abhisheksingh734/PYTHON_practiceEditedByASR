def division(a,b):
    print(a/b)
def newdiv(func):
    def innerfunc(a,b):
        if a < b:
            a,b=b,a
        return func(a,b) 
    return innerfunc
division = newdiv(division)
division(2,4)
