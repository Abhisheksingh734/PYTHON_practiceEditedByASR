x = str(input())
x1=int(x[0])
x2=int(x[-1])
ans = x1*x2
print(ans)

if ans%5==0 :
    print("True")
else :
    print("False")