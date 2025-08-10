str = input("Enter a string:\n")
vstr = "aeiouAEIOU"
v = 0
for i in str:
    if i in vstr:
        v+= 1
print(f"No. of Vowels in {str} is {v}")