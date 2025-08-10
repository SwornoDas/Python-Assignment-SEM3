import string
str = input("Enter a string:\n")

set_1 = string.ascii_letters
set_2 = string.digits
set_3 = string.punctuation

l = d = s = 0

for i in str:
    if i in set_1:
        l+= 1
    elif i in set_2:
        d+= 1
    else:
        s+= 1

print(f"No. of Letters in {str} is {l}")
print(f"No. of Digits in {str} is {d}")
print(f"No. of Special Characters in {str} is {s}")