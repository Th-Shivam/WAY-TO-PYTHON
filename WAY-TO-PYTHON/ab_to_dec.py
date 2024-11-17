BaseOfAS = int(input("Enter the base of the original number system: "))
UserNum = input("Enter the original characters (digits): ")  
Result = 0
length = len(UserNum)
for i in range(length - 1, -1, -1):
    Val1 = int(UserNum[i])  
    Val2 = BaseOfAS ** (length - 1 - i)  
    Result += Val1 * Val2
print("Converted to decimal:", Result)




    
    