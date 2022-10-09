marks = int(input("enter your marks :"))

if marks>90 and marks<=100:
    print ("Congratulations your grade is A") #and meaning : if input and output both are true then only it'll print
                                              # in and both conditions needs to be true 

elif marks>80 and marks<=90:
    print ("Congratulations your grade is B")    

elif marks>70 and marks<=80:
    print ("Congratulations your grade is C")    

elif marks>33 and marks <=70:
    print ("congratulations your grade is D")

elif marks>0 and marks<=33 :
    print ("sorry, you've failed,Your grade is F")

else:
    print ("your number is invalid.")    
    #or meaning : even if one of the input is true the output is true 