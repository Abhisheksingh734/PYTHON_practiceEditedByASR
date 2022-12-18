myset = {"car","boat","bike"}
if "boat" in myset:
    print("yes")

#union 
myset1={"car","boat","bike"}
myset2 = {1,2,3,4}
myset3 = [4,5,6,7]
Output = myset2.union(myset3)
print(Output)
#intersection
output1 = myset2.intersection(myset3)
print(output1)
#symmetric difference
output2=myset2.symmetric_difference(myset3) 
print(output2)