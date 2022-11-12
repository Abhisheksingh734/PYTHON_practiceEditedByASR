def biodata(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

biodata("Shubham",age=18,place = "delhi 41",number= 4557289032)