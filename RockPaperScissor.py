import random
print("LETS START THE GAME")
p1_input=str(input("please enter your choice: Rock/Paper/Scissor[make sure the spelling is correct]"))
ref_list=["Rock","Paper","Scissor"]
computer_input= random.choice (ref_list)

print("YOUR INPUT IS : ",p1_input)
print("COMPUTER'S INPUT IS : ",computer_input)

if p1_input==computer_input:
    print("ITS A TIE")
elif p1_input=="Rock" and computer_input=="Paper":
    print("YOU LOSE")
elif p1_input=="Paper"and computer_input=="Scissor":
    print("YOU LOSE")
elif p1_input=="Scissor"and computer_input=="Rock":
    print("YOU LOSE")
else:
    print("YOU DUMB AS HELL [CHECK SPELLING]")
