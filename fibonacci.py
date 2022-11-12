n = int(input())
a = 0
b = 1
sum = a+b
while n>0:
    print(a)
    a=b
    b=sum
    sum=a+b
    n-=1



