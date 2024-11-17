n = input("Enter the number : ")
userNum = int(n) 
print("You entered the number", userNum) 
if userNum > 20:
    print("You entered a number greater than 20, which is not permitted") 
while userNum > 20:
    n = input("Enter the number again: ")
    userNum = int(n)
    if userNum <= 20:
        print("You entered the number:", userNum)
        break

# First for loop 
for i in range(1, userNum + 1):
    if i <= 9:
        print(" " * (userNum - i) + " ".join([str(i)] * i))  # Spaces to align right
    else:
        print(" " * (userNum - i) + str(i) * i)
# Second for loop 
for i in range(userNum, 0, -1):
    if i <= 9:
        print(" " * (userNum - i) + " ".join([str(i)] * i))  # Spaces to align right
    else:
        print(" " * (userNum - i) + str(i) * i)
