# Method 1

# n = int(input())
# a = 0
# b = 1
# sum = a+b
# while n>0:
#     print(a)
#     a=b
#     b=sum
#     sum=a+b
#     n-=1



# Method 2
n=int(input("enter how many fibonacci numbers you wan to print: "))

fibo=[0,1]
[fibo.append(fibo[-1]+fibo[-2]) for i in range(n-2)]
print(fibo)