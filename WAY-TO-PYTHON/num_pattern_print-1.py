n = input("Enter the number : ")
userNum = int(n) 
print("You entered the number" , userNum) 
if(userNum>20):
    print("You entered a number greater than 20 , which is not permitted") 
while(userNum>20):
    n = input("Enter the number again : ")
    userNum=int(n)
    if(userNum<20):
       print("You entered the number :" , userNum)
       break
for i in range (1 , userNum+1):
     if (i <= 9):
        print(" ".join([str(i)] * i))  # two spaces between numbers
     else:
        print(str(i)*i)
    
for i in range (userNum , 0 , -1):
     if (i <= 9):
        print(" ".join([str(i)] * i))  # two spaces between numbers
     else:
        print(str(i)*i)
    
  
 