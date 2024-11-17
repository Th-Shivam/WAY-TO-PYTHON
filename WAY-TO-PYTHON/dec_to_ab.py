UserNum = int(input("Enter the decimal number: "))
BaseOfAS = int(input("Enter the base of the required number system: "))
Result = []

while UserNum > 0:
    Remainder = UserNum % BaseOfAS
    Quotient = UserNum // BaseOfAS
    Result.append(Remainder)
    UserNum = Quotient  

print("Converted result:", Result[::-1]) 
