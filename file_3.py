# Write a python program that calculates factorial of a given number:

num= int(input("Enter the number:"))
factorial=1

while(num>1):
    factorial=factorial*num
    num=num-1

print(factorial)
