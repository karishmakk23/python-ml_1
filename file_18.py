# Write a python program to check if the two strings are anagrams of each other:

str1=input("Enter the first string:")
str2=input("Enter the first string:")

str1=sorted(str1.lower())
str2=sorted(str2.lower())


if str1==str2:
    print("yes")
else:
    print("no")

