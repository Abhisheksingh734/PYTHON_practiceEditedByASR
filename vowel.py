input_string=str(input("please enter the vowels:"))
ref_string = "aeiouAEIOU"

if input_string in ref_string:
    print("yes",input_string,"is a vowel")
elif input_string not in ref_string:
    print("no",input_string,"is not a vowel")
    
else :
    print("invalid data")