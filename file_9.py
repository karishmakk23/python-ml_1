# Write a program to find out whether a substring is present in the given string:

str=input("Enter the string:")
sub_str=input("Enter the substring:")

if sub_str in str:
    print("This substring is a part of the string.")
else:
    print("This sub_str is not a part of the string.")