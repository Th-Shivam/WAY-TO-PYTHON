UserIn  = int(input("Enter the number till you want the Fibonacci series => "))
Ans = [0, 1]

def fibonacci(n):
    while len(Ans) < n:
        next_number = Ans[-1] + Ans[-2]  # Add the last two numbers in the list
        Ans.append(next_number)

fibonacci(UserIn)
print(Ans) 
