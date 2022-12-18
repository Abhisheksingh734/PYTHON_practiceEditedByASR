# dictionary are used to store data values in key value pair
mydictionary = {
    "name":"shubham",
    "age": 21,
    "class":"koc28",
    "percentage":"99%"
}
print(mydictionary)
#dictionaries are ordered in nature 
#duplicates are not allowed in dictionaries 
#changable/mutable

#length of the dictionary
print(len(mydictionary))
#get attribute 
get = mydictionary.get("age")
print(get)

a = mydictionary["name"]#another method 
print(a)

#to access all the keys in the dictionary 
keys = mydictionary.keys()
# for i in keys: can use for loop to print them individually
#     print(i)
print(keys)#output comes out in list
#pop method using key
z = mydictionary.pop("age")
print(mydictionary)#prints after popping age key from dictionary