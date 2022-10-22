name=str(input("please enter your name :"))
length= int(len(name))
if length%2!=0:
    print(name[length//2])
elif length%2==0:
    print(name[(length+1)//2])
else :
    print("invalid data.")