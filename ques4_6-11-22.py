list = ["atul","shubham","Anurag","Rahul","Dev","roy"]

def lenchecker(list):
    more = 0
    less = 0
        
    for i in list:
        x = len(i)
        if x>5:
            print(i)
            more+=1
        else :
            less+=1
    return  more,less
more,less = lenchecker(list)
print(less)
print(more)
