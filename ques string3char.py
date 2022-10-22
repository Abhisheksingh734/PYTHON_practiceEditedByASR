#if len >3 add ing
string=str(input("please enter the word:"))
length = int(len(string))
if length>3:
    print(string+"ing")
else:
    print("smaller than 3 characters.")