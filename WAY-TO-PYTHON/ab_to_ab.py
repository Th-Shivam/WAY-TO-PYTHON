#anybase to decimal 
BaseOfAS = int(input("Enter the base of the original number system: "))
UserNum = input("Enter the original characters (digits): ")  
Result1 = 0
length = len(UserNum)
for i in range(length - 1, -1, -1):
    Val1 = int(UserNum[i])  
    Val2 = BaseOfAS ** (length - 1 - i)  
    Result1 += Val1 * Val2

#decimal to anybase 

UserNum = Result1
BaseOfAS = int(input("Enter the base of the required number system: "))
Result = []

while UserNum > 0:
    Remainder = UserNum % BaseOfAS
    Quotient = UserNum // BaseOfAS
    Result.append(Remainder)
    UserNum = Quotient  

print("Converted result:", Result[::-1]) 

