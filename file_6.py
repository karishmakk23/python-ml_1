# Write a program that reads the content of a text file and prints it to the console:

file =input("Enter the name of the file in .txt format:")
file2=open(file,"r")
line=file2.readline()

while(line!=""):
    print(line)
    line=file2.readline()

file2.close()

