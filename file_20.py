#write a python program that takes a list of numbers and returns their sum:

#Taking list as input:

list=[]
n=int(input("Enter the no of elements:"))

for i in range(0 ,n):
    element=int(input())
    list.append(element)

print(list)

#Taking the sum of all elements :
sum=0

for i in range(0,n):
    sum=sum+list[i]

print(sum)

