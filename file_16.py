# WAP to count the frequency of each character in a string:

string =input("Enter the string:")
all_freq = {}

for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print("Count of all characters in string is :\n "
      + str(all_freq))



