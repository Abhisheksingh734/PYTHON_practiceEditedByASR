str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
str2 = "1234567890"
alph = 0
num = 0
x = str(input("please enter your text:"))
for i in x:
    if i in str1 and i not in str2:
        alph+=1
    elif i not in str1 and i  in str2:
        num+=1
if alph == 0 and num!=0:
    print("the input text only consists of numerics")
elif alph!=0 and num==0:
    print("the input text only consists of alphabets")
elif alph!=0 and num!=0 :
    print("the input text consists of both alphabets and numerics so its a alpha numeric text")
else : 
    print("invalid data :(")
print("number of alphabets:",alph)
print("number of numerics:",num)

