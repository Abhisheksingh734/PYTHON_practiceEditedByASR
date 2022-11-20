list = [32,21,64,100,13]
def oddevenchecker(list):
    even = 0
    odd = 0

    for i in list:
        if i % 2 == 0:
            even+=1
        else:
            odd +=1
    return even,odd

even,odd = oddevenchecker(list)

print(odd)
print(even)