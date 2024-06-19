# WAP to generate the first n numbers of a fabbonaci sequence:

n_terms=int(input("Enter the number of terms in the sequence:"))
n_1=0
n_2=1

count=0

if n_terms<=0:
    print("Enter the valid number")
elif n_terms==1:
    print("1")
else:
    while count<=n_terms :
        print(n_1)
        nth=n_1+n_2
        n_1=n_2
        n_2=nth
        count+=1






