def palin(str):
    revstr = str[::-1]

    if revstr == str:
        print("Palindrome String")
    else:
        print("Not a Palindorme String")
str = input("Enter a string:\n")
palin(str)