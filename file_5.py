# Write a program to take a string input from the user and writes it to a text file.

str_input= input("Enter your information :")

try:
    with open("python.txt","w") as python:
        python.write(str_input)
except:
    print("There is a problem")