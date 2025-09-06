def check(str):
    uc = lc = 0
    for i in str:
        if i.isupper():
            uc+= 1
        else:
            lc+= 1
    print(f"Number of Uppercase letter in '{str}' is {uc}")
    print(f"Number of Lowercase letter in '{str}' is {lc}")
str = input("Enter a string. ")
check(str.rstrip())