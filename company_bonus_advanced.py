#company will give bonus based on the following criteria
#time spent in company                bonus
#<10 years                            10%
#>=6 and <=10                         8%
#<6                                   5%
#input salary and time print net amount

salary = int (input("please enter your salary :"))
Time = int (input ("please enter the time you've been working in this company in years : "))
bonus10 = salary*(10/100) + salary
bonus8 = salary*(8/100) + salary
bonus5 = salary*(5/100) + salary
if Time > 10 and Time<100:
    print ("your salary plus the bonus amount is :", bonus10)
elif Time >= 6 and Time<10:    
    print("your salary plus the bonus amount is :", bonus8)
elif Time<6 and Time>=0:
    print("your salary plus the bonus amount is :", bonus5)
else:
    print("invalid data")      