# calculator program:

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Enter the operation (+ or _ or * or / or %) : ")

if operation=="+":
    sum=num1+num2
    print(sum)
if operation=="-":
    difference=num1-num2
    print(difference)
if operation==("*"):
    product=num1*num2
    print(product)
if operation == "/":
    quotient=num1/num2
    print(quotient)
if operation=="%":
    remainder=num1%num2
    print(remainder)

