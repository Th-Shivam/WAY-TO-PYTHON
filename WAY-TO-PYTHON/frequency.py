import matplotlib.pyplot as plt 

var1 = [5,10,20,15,5,20,20,15,15,15,10,10,10,20,15,5,18,18,18,18]

unique_values = []
for num in var1:
    if num not in unique_values:
        unique_values.append(num)
print(unique_values)

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

def check1(var1):
    for i in var1:
        if i == 5:
            list1.append(i)
    return list1
print(check1(var1))

def check10(var1):
    for i in var1:
        if i == 10:
            list2.append(i)
    return list2
print(check10(var1))

def check15(var1):
    for i in var1:
        if i == 15:
            list3.append(i)
    return list3
print(check15(var1))

def check18(var1):
    for i in var1:
        if i == 18:
            list4.append(i)
    return list4
print(check18(var1)) 

def check20(var1):
    for i in var1:
        if i == 20:
            list5.append(i)
    return list5
print(check20(var1))
print( "Frequency of 5 is" , len(list1) )
print("Frequency of 10 is" ,  len(list2))
print("Frequency of 15 is" ,  len(list3))
print("Frequency of 18 is" ,  len(list4))
print("Frequency of 20 is" ,  len(list5))

x = [5,10,15,18,20]
y = [len(list1) , len(list2) , len(list3) , len(list4) , len(list5)] 
plt.scatter(x,y)
plt.show()
